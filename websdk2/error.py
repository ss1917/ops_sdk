from enum import IntEnum
from .consts import ErrorCode
class BaseError(Exception):
    """ 错误基类，所有错误必须从该类继承 """

    def __init__(self, errorcode, *args, **kwargs):
        """
        初始化错误基类
        :param errorcode: 错误码
        :param args:
        :param kwargs:
        """
        if isinstance(errorcode, IntEnum):
            self._errorcode = errorcode
            self.kwargs = kwargs
            super(BaseError, self).__init__(*args)
        else:
            raise TypeError(
                'Error code must be vmbsdk.constants.enums.ErrorCode type.')

    @property
    def errorcode(self):
        return self._errorcode
class BizError(BaseError):
    """ 业务错误 """

    def __init__(self, errorcode, *args, **kwargs):
        self.__subcode = int(args[1]) if len(args) > 1 else 0
        super(BizError, self).__init__(errorcode, *args, **kwargs)

    @property
    def subcode(self):
        """
        获取
        :return:
        """
        return self.__subcode

class BadRequestError(BizError):
    """ 错误的请求 """

    def __init__(self, *args, **kwargs):
        super(BadRequestError, self).__init__(ErrorCode.bad_request,
                                              *args, **kwargs)


class ConfigError(Exception):
    def __init__(self, config_key, *args, **kwargs):
        self.config_key = config_key
        super(ConfigError, self).__init__(*args, **kwargs)