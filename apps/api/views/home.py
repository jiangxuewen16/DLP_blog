from core.lib.base_view import BaseView

@BaseView.route(path='/api/home/1')
class Home(BaseView):

    @BaseView.route(path='/api/home/')
    def index(self):

        return self.response(self.requestParam)

    @BaseView.route(path='/api/home/1')
    def home(self):
        return self.response(self.requestParam)

    @BaseView.route(path='/api/home/')
    def home1(self):
        return self.response(self.requestParam)


