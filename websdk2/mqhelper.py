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
import time
import json
from typing import Optional, Tuple, Union, List

from pika.exceptions import AMQPConnectionError, ChannelClosedByBroker
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
JsonOrBytes = Union[bytes, bytearray, str, dict, list]


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


class MessageQueueBaseV2:
    """
    消息队列基类：集成消费者和生产者功能。
    线程模型：推荐每个线程创建独立实例，不要跨线程共享（BlockingConnection 非线程安全）。
    """

    def __init__(self, exchange: str, exchange_type: str = "direct", routing_key: str = "",
                 routing_keys: Optional[List[str]] = None, queue_name: str = "",
                 no_ack: bool = False, mq_key: str = const.DEFAULT_MQ_KEY):

        # 读取配置
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

        # 拓扑与消费参数
        self.exchange = exchange
        self.exchange_type = exchange_type
        self.routing_key = routing_key
        self.routing_keys = routing_keys or []
        self.queue_name = queue_name
        self.no_ack = no_ack

        # 连接/通道
        self.connection: Optional[pika.BlockingConnection] = None
        self.channel: Optional[pika.adapters.blocking_connection.BlockingChannel] = None

        # 状态
        self._returned = []
        self._callbacks_ready = False
        self._blocked = False

        # 统一的连接参数（避免重复创建）
        self._conn_params = pika.ConnectionParameters(
            host=self.addr,
            port=self.port,
            virtual_host=self.vhost,
            credentials=pika.PlainCredentials(self.user, self.pwd),
            heartbeat=30,
            blocked_connection_timeout=300,
            connection_attempts=3,
            retry_delay=2.0,
        )

    # ========== Context Manager ==========
    def __enter__(self):
        self._ensure_conn_chan(need_confirm=False)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    # ========== 连接/通道管理 ==========
    def _ensure_conn_chan(self, need_confirm: bool = False) -> None:
        """
        确保连接和通道可用，并按需注册回调和确认机制。

        参数：
        - need_confirm: 是否需要发布确认（消费时 False，生产时 True）
        """
        # 确保连接可用
        if not (self.connection and self.connection.is_open):
            self.connection = pika.BlockingConnection(self._conn_params)
            self.connection.add_on_connection_blocked_callback(
                lambda c, r: self._on_blocked(r)
            )
            self.connection.add_on_connection_unblocked_callback(
                lambda c: self._on_unblocked()
            )
            self._callbacks_ready = False

        # 确保通道可用
        if not (self.channel and self.channel.is_open):
            self.channel = self.connection.channel()
            self._callbacks_ready = False

        # 按需注册发布确认和 return 回调（仅注册一次）
        if need_confirm and not self._callbacks_ready:
            self.channel.confirm_delivery()
            self._returned.clear()
            self.channel.add_on_return_callback(
                lambda ch, m, p, b: self._returned.append((m, p, b))
            )
            self._callbacks_ready = True

    def _on_blocked(self, reason: str):
        """broker 阻塞回调（内存/磁盘告警）"""
        self._blocked = True
        logger.warning(f"Connection blocked: {reason}")

    def _on_unblocked(self):
        """broker 解除阻塞回调"""
        self._blocked = False
        logger.info("Connection unblocked")

    def _close_resources(self) -> None:
        """关闭连接和通道（先关通道，再关连接）"""
        # 关闭通道
        if self.channel:
            try:
                if self.channel.is_open:
                    self.channel.close()
            except Exception:
                pass
            finally:
                self.channel = None

        # 关闭连接
        if self.connection:
            try:
                if self.connection.is_open:
                    self.connection.close()
            except Exception:
                pass
            finally:
                self.connection = None

        # 重置状态
        self._callbacks_ready = False
        self._returned.clear()

    def close(self):
        """关闭连接和通道"""
        self._close_resources()

    def _reset_connection(self) -> None:
        """异常时重置连接（同 close）"""
        self._close_resources()

    # ========== 消费 ==========
    def start_consuming(self, exchange_durable: bool = False):
        """开始消费消息"""
        self._ensure_conn_chan(need_confirm=False)
        self._declare_exchange(self.channel, exchange_durable)
        queue_name = self._declare_and_bind_queue(self.channel)

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=queue_name, on_message_callback=self._callback,
                                   auto_ack=self.no_ack)
        logger.info(f"[*] Queue {queue_name} started")
        self.channel.start_consuming()

    def _callback(self, ch, method, properties, body):
        """消息回调处理"""
        try:
            self.on_message(body)
            if not self.no_ack:
                ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception:
            logger.error("on_message error:\n%s", traceback.format_exc())
            if not self.no_ack:
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

    def on_message(self, body: bytes):
        """子类实现具体逻辑"""
        raise NotImplementedError

    # ========== 生产 ==========
    @staticmethod
    def _encode_body(body: JsonOrBytes, json_encode: bool) -> Tuple[bytes, str]:
        """
        编码消息体并推断 content_type。

        返回：(payload, content_type)
        """
        if isinstance(body, (bytes, bytearray)):
            return bytes(body), "application/octet-stream"
        if isinstance(body, str):
            return body.encode("utf-8"), "text/plain"
        if json_encode:
            return json.dumps(body, ensure_ascii=False).encode("utf-8"), "application/json"
        raise TypeError(f"body type {type(body)} not supported")

    def publish(self, exchange: str, routing_key: str, body: JsonOrBytes,
                durable: bool = True, json_encode: bool = True, mandatory: bool = True,
                max_retries: int = 6) -> None:
        """
        发送消息（可靠性：发布确认 + mandatory + return 机制）。

        参数：
        - exchange: 交换机名
        - routing_key: 路由键
        - body: 消息体 (str/bytes/dict/list)
        - durable: 是否持久化（默认 True）
        - json_encode: 是否 JSON 编码（默认 True）
        - mandatory: 是否强制要求有接收方（默认 True，无队列绑定时返回）
        - max_retries: 最大重试次数（默认 6）
        """
        # 检查 broker 是否阻塞
        if self._blocked:
            logger.warning("Broker is blocked, retrying may be needed")

        # 编码消息
        payload, actual_content_type = self._encode_body(body, json_encode)
        props = pika.BasicProperties(
            delivery_mode=2 if durable else 1,  # 2=持久化, 1=临时
            content_type=actual_content_type,
        )

        last_err = None
        for attempt in range(1, max_retries + 1):
            try:
                # 确保连接和通道可用（需要确认机制）
                self._ensure_conn_chan(need_confirm=True)

                # 清空返回列表
                self._returned.clear()

                # 发送消息
                self.channel.basic_publish(
                    exchange=exchange,
                    routing_key=routing_key,
                    body=payload,
                    properties=props,
                    mandatory=mandatory
                )

                # 检查消息是否被返回（无队列绑定）
                if self._returned:
                    raise RuntimeError(f"Message unroutable: no binding for routing_key={routing_key}")

                # logger.info(f"Message published: {exchange}/{routing_key}")
                return

            except (AMQPConnectionError, ChannelClosedByBroker) as e:
                # 网络错误 → 重试
                last_err = e
                logger.warning(f"Connection error on attempt {attempt}/{max_retries}: {e}")
                self._reset_connection()
                if attempt < max_retries:
                    time.sleep(min(2 ** attempt, 5))  # 指数退避

            except RuntimeError as e:
                # 业务错误（不可路由等）→ 不重试
                logger.error(f"Publish error: {e}")
                raise

            except Exception as e:
                # 其他异常 → 重试
                last_err = e
                logger.error(f"Unexpected error on attempt {attempt}/{max_retries}: {e}")
                self._reset_connection()
                if attempt < max_retries:
                    time.sleep(min(2 ** attempt, 5))

        raise last_err or RuntimeError("Unknown publish error")

    # ========== 私有辅助方法 ==========
    def _declare_exchange(self, ch, exchange_durable: bool):
        """声明交换机"""
        ch.exchange_declare(exchange=self.exchange,
                            exchange_type=self.exchange_type,
                            durable=exchange_durable)

    def _declare_and_bind_queue(self, ch):
        """声明队列并绑定"""
        # 声明队列
        if self.queue_name:
            result = ch.queue_declare(queue=self.queue_name, durable=True)
        else:
            result = ch.queue_declare(queue="", exclusive=True, auto_delete=True)

        queue_name = result.method.queue

        # 绑定队列
        if self.routing_keys:
            for rk in self.routing_keys:
                ch.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=rk)
        else:
            ch.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=self.routing_key)

        return queue_name
