from django.views import View

# Create your views here.
from core.lib.base_view import BaseView


class Home(BaseView):

    def index(self):
        return self.response(self.requestParam)
