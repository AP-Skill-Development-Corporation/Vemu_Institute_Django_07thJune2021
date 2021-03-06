"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',views.hai,name='hi'),
    path('hello/',views.hello,name='hello'),
    path('sample/',views.sample,name='sample'),
    path('home/<str:name>/',views.hm,name='home'),
    path('basic/<int:num>/',views.basic,name='basic'),
    path('task/<str:name>/<int:id>/',views.task,name='task'),
    path('temp/',views.temp,name='temp'),
    path('ls/<str:name>/<int:id>/',views.ls,name='ls'),
    path('table/',views.table,name='table'),
    path('inline/',views.inline,name='inline'),
    path('internal/',views.internal,name='internal'),
    path('external/',views.external,name='external'),
]
