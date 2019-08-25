from core.common.service_code import ServiceCode
from core.lib.view import BaseView
from core.lib.route import Route


@Route.route(path='/api/home')
class Home(BaseView):

    @Route.route(path='/api/home/')
    def index(self):
        return self.response(self.requestParam)

    @Route.route(path='/home/1')
    def home(self):
        return self.failure(ServiceCode.param_not_exists, {'a': 1})

    @Route.route(path='/api/home/')
    def home1(self):
        return self.response(self.requestParam)
