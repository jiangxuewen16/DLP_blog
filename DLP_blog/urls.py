"""DLP_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import importlib

from django.contrib import admin
from django.urls import path, include, re_path

from core.lib.route import Route

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'api/home', Home.as_view()),
]


"""
注册注解路由
"""
routeKeyList: list = []
for classItem in Route.classRoute:  # 类路由
    module = importlib.import_module(classItem.module)
    routeClass = getattr(module, classItem.class_name)
    for routeItem in Route.ROUTER:  # 方法路由
        if routeItem.module + routeItem.class_name == classItem.module + classItem.class_name:  # 是不是同一个类
            path = classItem.path + routeItem.path  # 路由路径
            if path in Route.routeList:
                exceptionStr = f'路由重复：{routeItem.module + routeItem.class_name} -> {routeItem.func_name}, 路径：{path}'
                raise Exception(exceptionStr)
            Route.routeList[path] = routeItem.func_name
            if classItem.path in routeKeyList:
                continue
            # print('============', classItem.path, routeClass)
            urlpatterns.append(re_path(r'^' + classItem.path, routeClass.as_view())),
            routeKeyList.append(classItem.path)

print('总路由:', urlpatterns)

