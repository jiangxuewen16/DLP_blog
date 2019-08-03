import json
from operator import methodcaller

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.views import View


class BaseView(View):
    requestParam: dict

    def init(self):
        self.requestParam = json.loads(self.request.body)

    """
    post 处理
    """
    def post(self, request: WSGIRequest):
        # print(dir(self.request))
        self.init()
        return methodcaller('index')(self)  # 自调方法

    """
    get 处理
    """
    def get(self, request: WSGIRequest) -> HttpResponse:
        pass

    @classmethod
    def response(cls, data: dict, contentType: str = 'application/json') -> HttpResponse:
        return HttpResponse(json.dumps(data), contentType)
