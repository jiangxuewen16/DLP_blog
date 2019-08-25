from core.common.service_code import ServiceCode
from core.lib.view import BaseView
from core.lib.route import Route


@Route.route(path='/api/user')
class User(BaseView):

    @Route.route(path='qqqqqq')
    def index(self):
        return self.response(self.requestParam)

    @Route.route(path='/get/1')
    def home(self):
        return self.failure(ServiceCode.param_not_exists, {'a': 1})
