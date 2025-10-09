# !/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : ming
date   : 2017/3/3 下午9:31
role   : rabbitMQ 操作类
"""

import logging
import traceback
import pika
from .consts import const
from .configs import configs
from .error import ConfigError

# 配置pika日志级别
logger = logging.getLogger('pika')
logger.setLevel(logging.ERROR)

# 屏蔽pika诊断日志噪音
pika_diagnostic_logger = logging.getLogger('pika.diagnostic_utils')
pika_diagnostic_logger.setLevel(logging.CRITICAL)

# 屏蔽pika适配器日志噪音
pika_adapter_logger = logging.getLogger('pika.adapters')
pika_adapter_logger.setLevel(logging.CRITICAL)


class MessageQueueBase:
    def __init__(self, exchange, exchange_type, routing_key="", routing_keys=None,
                 queue_name="", no_ack=False, mq_key=const.DEFAULT_MQ_KEY):

        mq_config = configs[const.MQ_CONFIG_ITEM].get(mq_key)
        if not mq_config:
            raise ConfigError(f"MQ config {mq_key} not found")

        required_keys = [const.MQ_ADDR, const.MQ_PORT, const.MQ_VHOST, const.MQ_USER, const.MQ_PWD]
        for k in required_keys:
            if k not in mq_config:
                raise ConfigError(k)

        self.addr = mq_config[const.MQ_ADDR]
        self.port = int(mq_config[const.MQ_PORT])
        self.vhost = mq_config[const.MQ_VHOST]
        self.user = mq_config[const.MQ_USER]
        self.pwd = mq_config[const.MQ_PWD]

        self.exchange = exchange
        self.exchange_type = exchange_type
        self.routing_key = routing_key
        self.routing_keys = routing_keys or []
        self.queue_name = queue_name
        self.no_ack = no_ack

        self.connection = None
        self.channel = None

    # ========== Context Manager ==========
    def __enter__(self):
        self.channel = self.create_channel()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    # ========== Connection / Channel ==========
    def create_channel(self):
        credentials = pika.PlainCredentials(self.user, self.pwd)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.addr, self.port, self.vhost, credentials=credentials)
        )
        self.channel = self.connection.channel()
        return self.channel

    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()

    def new_channel(self):
        self.channel = self.create_channel()
        return self

    # ========== Consume ==========
    def start_consuming(self, exchange_durable=False):
        ch = self.create_channel()
        self._declare_exchange(ch, exchange_durable)
        queue_name = self._declare_and_bind_queue(ch)

        ch.basic_qos(prefetch_count=1)
        ch.basic_consume(queue=queue_name, on_message_callback=self.call_back, auto_ack=self.no_ack)
        logger.info(f"[*] Queue {queue_name} started.")
        ch.start_consuming()

    def call_back(self, ch, method, properties, body):
        try:
            logger.info("Received message")
            self.on_message(body)
            if not self.no_ack:
                ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception:
            logger.error(traceback.format_exc())
            if not self.no_ack:
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

    def on_message(self, body):
        """子类实现具体逻辑"""
        raise NotImplementedError

    # ========== Publish ==========
    def publish_message(self, body, durable=True, exchange_durable=False):
        if not self.channel:
            self.create_channel()

        self._declare_exchange(self.channel, exchange_durable)
        queue_name = self._declare_and_bind_queue(self.channel)

        props = pika.BasicProperties(delivery_mode=2) if durable else None
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body=body,
            properties=props,
        )
        logger.info(f"Publish message success: {body} -> queue {queue_name}")

    # ========== Private Helpers ==========
    def _declare_exchange(self, ch, exchange_durable):
        ch.exchange_declare(exchange=self.exchange,
                            exchange_type=self.exchange_type,
                            durable=exchange_durable)

    def _declare_and_bind_queue(self, ch):
        if self.queue_name:
            result = ch.queue_declare(queue=self.queue_name, durable=True)
        else:
            result = ch.queue_declare(queue="", exclusive=True, auto_delete=True)

        queue_name = result.method.queue
        if self.routing_keys:
            for binding_key in self.routing_keys:
                ch.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=binding_key)
        else:
            ch.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=self.routing_key)
        return queue_name
