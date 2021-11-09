#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : ming
date   : 2017/3/3 下午9:31
role   : rabbitMQ 操作类
"""
import traceback
import pika
from .consts import const
from .configs import configs
from .web_logs import ins_log
from .error import ConfigError


class MessageQueueBase(object):
    def __init__(self, exchange, exchange_type, routing_key='', routing_keys=None, queue_name='', no_ack=False,
                 mq_key=const.DEFAULT_MQ_KEY):
        mq_config = configs[const.MQ_CONFIG_ITEM][mq_key]
        if const.MQ_ADDR not in mq_config:
            raise ConfigError(const.MQ_ADDR)
        if const.MQ_PORT not in mq_config:
            raise ConfigError(const.MQ_PORT)
        if const.MQ_VHOST not in mq_config:
            raise ConfigError(const.MQ_VHOST)
        if const.MQ_USER not in mq_config:
            raise ConfigError(const.MQ_USER)
        if const.MQ_PWD not in mq_config:
            raise ConfigError(const.MQ_PWD)
        self.addr = mq_config[const.MQ_ADDR]
        self.port = int(mq_config[const.MQ_PORT])
        self.vhost = mq_config[const.MQ_VHOST]
        self.user = mq_config[const.MQ_USER]
        self.pwd = mq_config[const.MQ_PWD]
        self.__exchange = exchange
        self.__exchange_type = exchange_type
        self.__routing_key = routing_key
        self.__routing_keys = routing_keys
        self.__queue_name = queue_name
        self.__no_ack = no_ack

    def start_consuming(self, exchange_durable=False):
        channel = self.create_channel()

        channel.exchange_declare(exchange=self.__exchange, exchange_type=self.__exchange_type, durable=exchange_durable)
        if self.__queue_name:
            result = channel.queue_declare(queue=self.__queue_name, durable=True)
        else:
            result = channel.queue_declare(exclusive=True)
        if self.__routing_keys and isinstance(self.__routing_keys, list):
            for binding_key in self.__routing_keys:
                channel.queue_bind(exchange=self.__exchange, queue=result.method.queue, routing_key=binding_key)
        else:
            channel.queue_bind(exchange=self.__exchange, queue=result.method.queue, routing_key=self.__routing_key)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(self.call_back, queue=result.method.queue, no_ack=self.__no_ack)
        ins_log.read_log('info', '[*]Queue %s started.' % (result.method.queue))

        channel.start_consuming()

    def __enter__(self):
        self.__channel = self.create_channel()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__connection.close()

    def close_channel(self):
        self.__connection.close()

    def create_channel(self):
        credentials = pika.PlainCredentials(self.user, self.pwd)
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.addr, self.port, self.vhost, credentials=credentials))
        channel = self.__connection.channel()
        return channel

    def call_back(self, ch, method, properties, body):
        try:
            ins_log.read_log('info', 'get message')
            self.on_message(body)

            if not self.__no_ack:
                ch.basic_ack(delivery_tag=method.delivery_tag)
        except:
            ins_log.read_log('error', traceback.format_exc())
            if not self.__no_ack:
                ch.basic_nack(delivery_tag=method.delivery_tag)

    def on_message(self, body):
        pass

    def publish_message(self, body, durable=True, exchange_durable=False):
        self.__channel.exchange_declare(exchange=self.__exchange, exchange_type=self.__exchange_type,
                                        durable=exchange_durable)
        if self.__queue_name:
            result = self.__channel.queue_declare(queue=self.__queue_name)
        else:
            result = self.__channel.queue_declare(exclusive=True, auto_delete=True)

        self.__channel.queue_bind(exchange=self.__exchange, queue=result.method.queue)

        if durable:
            properties = pika.BasicProperties(delivery_mode=2)
            self.__channel.basic_publish(exchange=self.__exchange, routing_key=self.__routing_key, body=body,
                                         properties=properties)
        else:
            self.__channel.basic_publish(exchange=self.__exchange, routing_key=self.__routing_key, body=body)
        ins_log.read_log('info', 'Publish message %s sucessfuled.' % body)
