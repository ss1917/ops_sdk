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
import threading
from typing import Optional, List, Dict, Any, Callable
from .consts import const
from .configs import configs
from .error import ConfigError

# 配置pika日志级别
pika_logger = logging.getLogger('pika')
pika_logger.setLevel(logging.ERROR)

# 屏蔽pika诊断日志噪音
pika_diagnostic_logger = logging.getLogger('pika.diagnostic_utils')
pika_diagnostic_logger.setLevel(logging.CRITICAL)

# 屏蔽pika适配器日志噪音
pika_adapter_logger = logging.getLogger('pika.adapters')
pika_adapter_logger.setLevel(logging.CRITICAL)


# class MessageQueueBase(object):
#     def __init__(self, exchange, exchange_type, routing_key='', routing_keys=None, queue_name='', no_ack=False,
#                  mq_key=const.DEFAULT_MQ_KEY):
#         mq_config = configs[const.MQ_CONFIG_ITEM][mq_key]
#         if const.MQ_ADDR not in mq_config:
#             raise ConfigError(const.MQ_ADDR)
#         if const.MQ_PORT not in mq_config:
#             raise ConfigError(const.MQ_PORT)
#         if const.MQ_VHOST not in mq_config:
#             raise ConfigError(const.MQ_VHOST)
#         if const.MQ_USER not in mq_config:
#             raise ConfigError(const.MQ_USER)
#         if const.MQ_PWD not in mq_config:
#             raise ConfigError(const.MQ_PWD)
#         self.addr = mq_config[const.MQ_ADDR]
#         self.port = int(mq_config[const.MQ_PORT])
#         self.vhost = mq_config[const.MQ_VHOST]
#         self.user = mq_config[const.MQ_USER]
#         self.pwd = mq_config[const.MQ_PWD]
#         self.__exchange = exchange
#         self.__exchange_type = exchange_type
#         self.__routing_key = routing_key
#         self.__routing_keys = routing_keys
#         self.__queue_name = queue_name
#         self.__no_ack = no_ack
#         self.__channel = None
#         self.__connection = None
#
#     def start_consuming(self, exchange_durable=False):
#         channel = self.create_channel()
#
#         channel.exchange_declare(exchange=self.__exchange, exchange_type=self.__exchange_type, durable=exchange_durable)
#         if self.__queue_name:
#             result = channel.queue_declare(queue=self.__queue_name, durable=True)
#         else:
#             result = channel.queue_declare('', exclusive=True)
#         if self.__routing_keys and isinstance(self.__routing_keys, list):
#             for binding_key in self.__routing_keys:
#                 channel.queue_bind(exchange=self.__exchange, queue=result.method.queue, routing_key=binding_key)
#         else:
#             channel.queue_bind(exchange=self.__exchange, queue=result.method.queue, routing_key=self.__routing_key)
#
#         channel.basic_qos(prefetch_count=1)
#         channel.basic_consume(result.method.queue, self.call_back, self.__no_ack)
#         logging.info('[*]Queue %s started.' % (result.method.queue))
#
#         channel.start_consuming()
#
#     def __enter__(self):
#         self.__channel = self.create_channel()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.__connection.close()
#
#     def close_channel(self):
#         self.__connection.close()
#
#     def create_channel(self):
#         credentials = pika.PlainCredentials(self.user, self.pwd)
#         self.__connection = pika.BlockingConnection(
#             pika.ConnectionParameters(self.addr, self.port, self.vhost, credentials=credentials))
#         channel = self.__connection.channel()
#         return channel
#
#     def new_channel(self):
#         self.__channel = self.create_channel()
#         return self
#
#     def call_back(self, ch, method, properties, body):
#         try:
#             logging.info('get message')
#             self.on_message(body)
#
#             if not self.__no_ack:
#                 ch.basic_ack(delivery_tag=method.delivery_tag)
#         except:
#             logging.error(traceback.format_exc())
#             if not self.__no_ack:
#                 ch.basic_nack(delivery_tag=method.delivery_tag)
#
#     def on_message(self, body):
#         pass
#
#     def publish_message(self, body, durable=True, exchange_durable=False):
#         self.__channel.exchange_declare(exchange=self.__exchange, exchange_type=self.__exchange_type,
#                                         durable=exchange_durable)
#         if self.__queue_name:
#             result = self.__channel.queue_declare(queue=self.__queue_name)
#         else:
#             result = self.__channel.queue_declare("", exclusive=True, auto_delete=True)
#
#         self.__channel.queue_bind(exchange=self.__exchange, queue=result.method.queue)
#
#         if durable:
#             properties = pika.BasicProperties(delivery_mode=2)
#             self.__channel.basic_publish(exchange=self.__exchange, routing_key=self.__routing_key, body=body,
#                                          properties=properties)
#         else:
#             self.__channel.basic_publish(exchange=self.__exchange, routing_key=self.__routing_key, body=body)
#         logging.info('Publish message %s sucessfuled.' % body)
class RabbitMQConnectionPool:
    """RabbitMQ连接池管理器 - 实现一个应用一个连接的最佳实践"""

    _connections: Dict[str, Optional[pika.BlockingConnection]] = {}
    _connection_lock = threading.Lock()

    @classmethod
    def get_connection(cls, mq_key: str = const.DEFAULT_MQ_KEY) -> pika.BlockingConnection:
        """获取或创建连接"""
        if mq_key not in cls._connections or not cls._is_connection_healthy(mq_key):
            with cls._connection_lock:
                # 双重检查锁定
                if mq_key not in cls._connections or not cls._is_connection_healthy(mq_key):
                    cls._create_connection(mq_key)

        return cls._connections[mq_key]

    @classmethod
    def _create_connection(cls, mq_key: str) -> None:
        """创建新连接"""
        try:
            # 清理旧连接
            cls._cleanup_connection(mq_key)

            # 获取并验证配置
            mq_config = configs[const.MQ_CONFIG_ITEM][mq_key]
            cls._validate_config(mq_config)

            # 创建连接参数，优化超时和重试设置
            credentials = pika.PlainCredentials(
                mq_config[const.MQ_USER],
                mq_config[const.MQ_PWD]
            )

            connection_params = pika.ConnectionParameters(
                host=mq_config[const.MQ_ADDR],
                port=int(mq_config[const.MQ_PORT]),
                virtual_host=mq_config[const.MQ_VHOST],
                credentials=credentials,
                heartbeat=600,  # 减少心跳间隔
                blocked_connection_timeout=300,  # 减少阻塞超时
                socket_timeout=60,  # 添加socket超时
                connection_attempts=2,  # 连接重试次数
                retry_delay=2,  # 重试延迟
                stack_timeout=60  # 栈超时
            )

            connection = pika.BlockingConnection(connection_params)

            # 验证连接状态
            if not connection.is_open:
                raise Exception("Connection failed to open properly")

            cls._connections[mq_key] = connection
            logging.info(f"Created new RabbitMQ connection for key: {mq_key}")

        except Exception as e:
            logging.error(f"Failed to create connection for {mq_key}: {e}")
            cls._connections[mq_key] = None
            raise

    @classmethod
    def _is_connection_healthy(cls, mq_key: str) -> bool:
        """检查连接健康状态"""
        connection = cls._connections.get(mq_key)
        try:
            return connection and connection.is_open
        except Exception:
            return False

    @classmethod
    def _cleanup_connection(cls, mq_key: str) -> None:
        """清理旧连接"""
        old_connection = cls._connections.get(mq_key)
        if old_connection:
            try:
                old_connection.close()
                logging.debug(f"Cleaned up old connection for {mq_key}")
            except Exception as e:
                logging.warning(f"Error cleaning up connection {mq_key}: {e}")

    @classmethod
    def _validate_config(cls, mq_config: Dict[str, Any]) -> None:
        """验证MQ配置"""
        required_keys = [const.MQ_ADDR, const.MQ_PORT, const.MQ_VHOST, const.MQ_USER, const.MQ_PWD]
        for key in required_keys:
            if key not in mq_config:
                raise ConfigError(key)

    @classmethod
    def close_all_connections(cls) -> None:
        """关闭所有连接"""
        with cls._connection_lock:
            for mq_key, connection in cls._connections.items():
                if connection:
                    try:
                        connection.close()
                        logging.info(f"Closed connection for {mq_key}")
                    except Exception as e:
                        logging.warning(f"Error closing connection {mq_key}: {e}")
            cls._connections.clear()
            logging.info("All connections closed")

    @classmethod
    def get_connection_status(cls) -> Dict[str, Any]:
        """获取所有连接的状态"""
        status = {}
        for mq_key, connection in cls._connections.items():
            status[mq_key] = {
                'exists': connection is not None,
                'is_open': cls._is_connection_healthy(mq_key)
            }
        return status


class MessageQueueBase:

    def __init__(self, exchange: str, exchange_type: str, routing_key: str = '',
                 routing_keys: Optional[List[str]] = None, queue_name: str = '',
                 no_ack: bool = False, mq_key: str = const.DEFAULT_MQ_KEY,
                 max_retries: int = 3):
        """初始化MessageQueue"""
        self._exchange = exchange
        self._exchange_type = exchange_type
        self._routing_key = routing_key
        self._routing_keys = routing_keys or []
        self._queue_name = queue_name
        self._no_ack = no_ack
        self._mq_key = mq_key
        self._max_retries = max_retries

        self.logger = logging.getLogger(f"{self.__class__.__name__}_{exchange}")
        self._lock = threading.Lock()

        # 如果queue_name为空，记录告警（但不阻止实例化，因为发布者不需要队列名）
        if not queue_name:
            self.logger.warning(
                f"[WARNING] MessageQueue created without queue_name. "
                f"Exchange: {exchange}, Type: {exchange_type}, RoutingKey: {routing_key}. "
                f"This is only acceptable for publishers. If you plan to consume messages, "
                f"you must provide a queue_name to avoid anonymous queues."
            )

    def _get_channel(self) -> Any:
        """获取新的通道 - 使用更安全的方式避免pika并发Bug"""
        max_attempts = 2  # 减少重试次数避免过度重试

        for attempt in range(max_attempts):
            try:
                # 每次都创建新连接，避免连接复用导致的并发问题
                if attempt > 0:
                    # 强制清理并等待
                    with RabbitMQConnectionPool._connection_lock:
                        try:
                            if self._mq_key in RabbitMQConnectionPool._connections:
                                RabbitMQConnectionPool._cleanup_connection(self._mq_key)
                                RabbitMQConnectionPool._connections[self._mq_key] = None
                        except:
                            pass

                    # 等待稍长时间让连接完全清理
                    time.sleep(0.5)

                connection = RabbitMQConnectionPool.get_connection(self._mq_key)
                if not connection:
                    raise Exception("Failed to get connection")

                # 简化状态检查，避免触发pika内部Bug
                if hasattr(connection, 'is_open') and not connection.is_open:
                    raise Exception("Connection is not open")

                # 直接创建channel，不做额外的心跳检查
                channel = connection.channel()
                if not channel:
                    raise Exception("Failed to create channel")

                if hasattr(channel, 'is_open') and not channel.is_open:
                    raise Exception("Channel is not open")

                return channel

            except Exception as e:
                self.logger.warning(f"Failed to get channel (attempt {attempt + 1}/{max_attempts}): {e}")
                if attempt == max_attempts - 1:
                    # 最后一次失败，创建一个临时连接
                    try:
                        return self._create_emergency_channel()
                    except Exception as emergency_e:
                        raise Exception(f"All channel attempts failed. Last error: {e}, Emergency error: {emergency_e}")

        raise Exception("Unexpected error in channel creation")

    def _create_emergency_channel(self) -> Any:
        """创建紧急通道 - 直接连接，不使用连接池"""
        try:
            mq_config = configs[const.MQ_CONFIG_ITEM][self._mq_key]

            credentials = pika.PlainCredentials(
                mq_config[const.MQ_USER],
                mq_config[const.MQ_PWD]
            )

            # 使用最简单的连接参数
            connection_params = pika.ConnectionParameters(
                host=mq_config[const.MQ_ADDR],
                port=int(mq_config[const.MQ_PORT]),
                virtual_host=mq_config[const.MQ_VHOST],
                credentials=credentials,
                heartbeat=0,  # 禁用心跳
                socket_timeout=10
            )

            connection = pika.BlockingConnection(connection_params)
            channel = connection.channel()

            self.logger.info("Created emergency channel")
            return channel

        except Exception as e:
            self.logger.error(f"Failed to create emergency channel: {e}")
            raise

    def _with_retry(self, operation: Callable, *args, **kwargs) -> Any:
        """带重试机制执行操作 - 优化版本"""
        last_exception = None

        for attempt in range(self._max_retries + 1):
            try:
                return operation(*args, **kwargs)
            except Exception as e:
                last_exception = e
                if attempt == self._max_retries:
                    self.logger.error(f"All {self._max_retries + 1} attempts failed: {e}")
                    break
                else:
                    self.logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")

                    # 只在特定错误类型时清理连接
                    error_str = str(e).lower()
                    if any(keyword in error_str for keyword in [
                        'connection', 'channel', 'socket', 'transport',
                        'callback', 'deque', 'abort', 'closed', 'asynctransport'
                    ]):
                        # 安全地清理连接
                        with RabbitMQConnectionPool._connection_lock:
                            try:
                                if self._mq_key in RabbitMQConnectionPool._connections:
                                    RabbitMQConnectionPool._cleanup_connection(self._mq_key)
                                    RabbitMQConnectionPool._connections[self._mq_key] = None
                            except Exception as cleanup_e:
                                self.logger.debug(f"Error during connection cleanup: {cleanup_e}")

                    # 递增延迟重试，但不要太长
                    time.sleep(min(0.1 * (2 ** attempt), 2.0))

        raise last_exception

    def close(self):
        """显式关闭方法"""
        self.logger.debug(f"MessageQueue instance for {self._exchange} closed")

    # ==================== 发布消息接口 ====================

    def publish(self, body: Any, routing_key: Optional[str] = None,
                durable: bool = True, exchange_durable: bool = False,
                queue_durable: bool = None) -> None:  # 🔥 新增参数：允许单独控制队列持久性
        """发布消息"""

        def _publish_operation():
            channel = self._get_channel()
            try:
                actual_routing_key = routing_key or self._routing_key

                # 声明交换机
                channel.exchange_declare(
                    exchange=self._exchange,
                    exchange_type=self._exchange_type,
                    durable=exchange_durable
                )

                # 如果有队列名，声明并绑定队列
                if self._queue_name:
                    # 🔥 修改：支持单独控制队列持久性，解决队列配置冲突问题
                    actual_queue_durable = queue_durable if queue_durable is not None else durable
                    channel.queue_declare(queue=self._queue_name, durable=actual_queue_durable)
                    channel.queue_bind(
                        exchange=self._exchange,
                        queue=self._queue_name,
                        routing_key=actual_routing_key
                    )

                # 发布消息
                properties = pika.BasicProperties(delivery_mode=2) if durable else None
                channel.basic_publish(
                    exchange=self._exchange,
                    routing_key=actual_routing_key,
                    body=body,
                    properties=properties
                )

                self.logger.info(
                    f'Published message to exchange:{self._exchange}, routing_key:{actual_routing_key}')

            finally:
                if channel and hasattr(channel, 'is_open') and channel.is_open:
                    try:
                        channel.close()
                    except:
                        pass  # 忽略关闭时的错误

        self._with_retry(_publish_operation)

    # ==================== 消费消息接口 ====================

    def start_consuming(self, exchange_durable: bool = False, callback: Optional[Callable] = None) -> None:
        """开始消费消息"""

        def _consume_operation():
            channel = self._get_channel()
            try:
                # 声明交换机
                channel.exchange_declare(exchange=self._exchange, exchange_type=self._exchange_type,
                                         durable=exchange_durable)
                # 声明队列
                if self._queue_name:
                    result = channel.queue_declare(queue=self._queue_name, durable=True)
                else:
                    result = channel.queue_declare('', exclusive=True)

                # 绑定路由键
                if self._routing_keys:
                    for binding_key in self._routing_keys:
                        channel.queue_bind(
                            exchange=self._exchange,
                            queue=result.method.queue,
                            routing_key=binding_key
                        )
                else:
                    channel.queue_bind(
                        exchange=self._exchange,
                        queue=result.method.queue,
                        routing_key=self._routing_key
                    )

                # 设置QoS
                channel.basic_qos(prefetch_count=1)

                # 设置消费回调
                message_callback = callback or self.call_back
                channel.basic_consume(result.method.queue, message_callback, self._no_ack)

                self.logger.info(f'[*]Queue {result.method.queue} started consuming')

                # 开始消费（这会阻塞）
                channel.start_consuming()

            except KeyboardInterrupt:
                self.logger.info("Received interrupt signal, stopping consumption")
                if channel and hasattr(channel, 'is_open') and channel.is_open:
                    try:
                        channel.stop_consuming()
                    except:
                        pass
            finally:
                if channel and hasattr(channel, 'is_open') and channel.is_open:
                    try:
                        channel.close()
                    except:
                        pass

        self._with_retry(_consume_operation)

    def call_back(self, ch: Any, method: Any, properties: Any, body: bytes) -> None:
        """默认消息回调处理"""
        try:
            self.logger.info('Received message')
            self.on_message(body)

            if not self._no_ack:
                ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            self.logger.error(f"Message processing failed: {e}\n{traceback.format_exc()}")
            if not self._no_ack:
                ch.basic_nack(delivery_tag=method.delivery_tag)

    def on_message(self, body: bytes) -> None:
        """消息处理方法，子类可重写"""
        pass

    # ==================== 向后兼容接口 ====================

    def create_channel(self) -> Any:
        """创建通道（向后兼容）"""
        return self._get_channel()

    def new_channel(self) -> 'MessageQueueBase':
        """创建新通道（向后兼容）"""
        RabbitMQConnectionPool.get_connection(self._mq_key)
        return self

    def check(self) -> None:
        """检查连接状态（向后兼容）"""
        try:
            connection = RabbitMQConnectionPool.get_connection(self._mq_key)
            if not connection.is_open:
                RabbitMQConnectionPool._connections[self._mq_key] = None
                RabbitMQConnectionPool.get_connection(self._mq_key)
        except Exception as e:
            self.logger.warning(f"Connection check failed: {e}")
            RabbitMQConnectionPool._connections[self._mq_key] = None

    # 统一的向后兼容发布方法
    def publish_message(self, body: Any, durable: bool = True, exchange_durable: bool = False,
                       queue_durable: bool = None) -> None:  # 🔥 新增参数：向后兼容方法也支持队列持久性控制
        """向后兼容的发布方法"""
        self.publish(body, durable=durable, exchange_durable=exchange_durable, queue_durable=queue_durable)

    def close_channel(self) -> None:
        """关闭连接（向后兼容）"""
        RabbitMQConnectionPool._cleanup_connection(self._mq_key)

    # ==================== 上下文管理器支持 ====================

    def __enter__(self) -> 'MessageQueueBase':
        """进入上下文管理器"""
        RabbitMQConnectionPool.get_connection(self._mq_key)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """退出上下文管理器"""
        self.close()

    # ==================== 工具方法 ====================

    def get_connection_status(self) -> Dict[str, Any]:
        """获取连接状态信息"""
        return {
            'mq_key': self._mq_key,
            'exchange': self._exchange,
            'exchange_type': self._exchange_type,
            'routing_key': self._routing_key,
            'queue_name': self._queue_name,
            'connection_healthy': RabbitMQConnectionPool._is_connection_healthy(self._mq_key),
            'max_retries': self._max_retries
        }


# ==================== 便捷工厂函数 ====================

def create_publisher(exchange: str, exchange_type: str, routing_key: str = '',
                     mq_key: str = const.DEFAULT_MQ_KEY, **kwargs) -> MessageQueueBase:
    """创建发布者实例"""
    return MessageQueueBase(exchange, exchange_type, routing_key, mq_key=mq_key, **kwargs)


def create_consumer(exchange: str, exchange_type: str, queue_name: str,
                    routing_key: str = '', routing_keys: Optional[List[str]] = None,
                    mq_key: str = const.DEFAULT_MQ_KEY, **kwargs) -> MessageQueueBase:
    """创建消费者实例"""
    return MessageQueueBase(exchange, exchange_type, routing_key, routing_keys,
                            queue_name, mq_key=mq_key, **kwargs)


def publish_once(exchange: str, exchange_type: str, message: Any,
                 routing_key: str = '', durable: bool = True,
                 exchange_durable: bool = False, mq_key: str = const.DEFAULT_MQ_KEY) -> None:
    """一次性发布消息的便捷函数"""
    try:
        with create_publisher(exchange, exchange_type, routing_key, mq_key) as publisher:
            publisher.publish(message, durable=durable, exchange_durable=exchange_durable)
            logging.info(f"Successfully published one-time message to {exchange}:{routing_key}")
    except Exception as e:
        logging.error(f"Failed to publish one-time message to {exchange}:{routing_key} - {e}")
        raise


# ==================== 使用示例 ====================

if __name__ == "__main__":
    # 示例1：推荐方式 - 使用上下文管理器
    print("=== 推荐方式：上下文管理器 ===")
    with create_publisher('test_exchange', 'direct', 'test.key') as publisher:
        publisher.publish("Hello with auto resource management!")

    # 示例2：一次性发布 - 最简单的方式
    print("=== 一次性发布 ===")
    publish_once('test_exchange', 'direct', "One-time message", 'test.key')

    # 示例3：向后兼容的使用方式
    print("=== 向后兼容使用 ===")
    with MessageQueueBase('test_exchange', 'direct', routing_key='test.key', queue_name='task_test_queue') as old_mq:
        old_mq.publish_message("Hello from old interface!")