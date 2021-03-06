# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _Yc


class _Serverless(_Yc):
    _type = "serverless"
    _icon_dir = "resources/yc/serverless"


class ApiGateway(_Serverless):
    _icon = "api-gateway.png"


class Functions(_Serverless):
    _icon = "functions.png"


class IotCore(_Serverless):
    _icon = "iot-core.png"


class MessageQueue(_Serverless):
    _icon = "message-queue.png"


class ServerlessFunctions(_Serverless):
    _icon = "serverless-functions.png"


class ServerlessTriggers(_Serverless):
    _icon = "serverless-triggers.png"


class YDB(_Serverless):
    _icon = "ydb.png"


# Aliases

IoT = IotCore
YMQ = MessageQueue
