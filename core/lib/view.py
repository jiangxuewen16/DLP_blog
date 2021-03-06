import json
import time
from operator import methodcaller

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.views import View

from core.common.service_code import ServiceCode
from core.lib.route import Route

"""
基础view类型
"""


class BaseView(View):
    request_param: dict = {}  # 请求数据

    def __init(self):
        request = json.loads(self.request.body)
        print(type(request))
        self.request_param = request['data']
        self.version = request['head']['version']
        self.time = request['head']['time']
        self.token = request['head']['token']
        self.platform = request['head']['platform']

    """
    post 处理
    """

    def post(self, request: WSGIRequest):
        self.__init()
        if request.path_info not in Route.routeList:
            pass
        print(Route.routeList, request.path_info.lstrip('/'))
        return methodcaller(Route.routeList[request.path_info.lstrip('/')])(self)  # 自调方法

    """
    get 处理
    """

    def get(self, request: WSGIRequest) -> HttpResponse:
        pass

    """
    统一返回操作
    """

    @classmethod
    def __response(cls, data: dict, service_code: ServiceCode, content_type: str = 'application/json') -> HttpResponse:
        response: dict = {'head': {'token': '', 'time': int(time.time()), 'code': service_code.value.code,
                                   'message': service_code.value.msg}, 'data': data}

        return HttpResponse(json.dumps(response), content_type)

    """
    成功返回方法
    """

    @classmethod
    def success(cls, data: dict, service_code: ServiceCode = ServiceCode.other_success) -> HttpResponse:
        return cls.__response(data, service_code)

    """
    失败返回方法
    """

    @classmethod
    def failure(cls, service_code: ServiceCode = ServiceCode.other_failure, data: dict = None) -> HttpResponse:
        return cls.__response(data, service_code)
