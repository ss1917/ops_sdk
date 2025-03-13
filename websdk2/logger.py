#!/usr/bin/env python
# -*-coding:utf-8-*-

import logging
import sys
import datetime
import tornado.log

#
# options.log_file_prefix = os.path.join(os.path.dirname(os.path.dirname(__file__)), f'/tmp/codo.log')


# class LogFormatter(tornado.log.LogFormatter):
#     default_msec_format = '%s.%03d'
#
#     def __init__(self):
#         super(LogFormatter, self).__init__(
#             fmt='%(color)s%(asctime)s | %(levelname)s%(end_color)s     | %(filename)s:%(funcName)s:%(lineno)s - %(message)s',
#             datefmt='%Y-%m-%d %H:%M:%S.%f'
#         )
#
#     def formatTime(self, record, datefmt=None):
#         ct = datetime.datetime.now()
#         t = ct.strftime(self.default_time_format)
#         s = self.default_msec_format % (t, record.msecs)
#         return s
#
#
# def init_logging():
#     # write file
#     [
#         i.setFormatter(LogFormatter())
#         for i in logging.getLogger().handlers
#     ]
#     logging.getLogger().setLevel(logging.INFO)
#     # write stdout
#     stdout_handler = logging.StreamHandler(sys.stdout)
#     stdout_handler.setFormatter(LogFormatter())
#     logging.getLogger().addHandler(stdout_handler)
#     logging.info('[APP Logging Init] logging has been started')


class LogFormatter(tornado.log.LogFormatter):
    """
    Custom log formatter to add color and detailed information to logs.
    """
    default_msec_format = '%s.%03d'

    def __init__(self):
        super(LogFormatter, self).__init__(
            fmt='%(color)s%(asctime)s | %(levelname)s%(end_color)s | '
                '%(filename)s:%(funcName)s:%(lineno)d - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S.%f'
        )

    def formatTime(self, record, datefmt=None):
        """
        Customize the timestamp format to include milliseconds.
        """
        ct = datetime.datetime.fromtimestamp(record.created)
        t = ct.strftime(self.default_time_format)
        s = self.default_msec_format % (t, record.msecs)
        return s


def init_logging(log_level=logging.INFO):
    """
    Initialize the logging system with custom formatter and handlers.

    :param log_level: Logging level, e.g., logging.DEBUG, logging.INFO, etc.
    """
    # Apply the custom formatter to existing handlers
    for handler in logging.getLogger().handlers:
        handler.setFormatter(LogFormatter())

    # Set the log level
    logging.getLogger().setLevel(log_level)

    # Add a handler for stdout logging
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(LogFormatter())
    logging.getLogger().addHandler(stdout_handler)

    logging.info(f'[APP Logging Init] Logging initialized with level: {logging.getLevelName(log_level)}')


# Example usage
if __name__ == "__main__":
    # Pass the desired log level as a parameter
    # log_level = logging.DEBUG  # You can adjust this to logging.INFO, logging.WARNING, etc.
    # init_logging(log_level)
    #
    # # Test logging at different levels
    # logging.debug("This is a debug message")
    # logging.info("This is an info message")
    # logging.warning("This is a warning message")
    # logging.error("This is an error message")
    # logging.critical("This is a critical message")
    pass
