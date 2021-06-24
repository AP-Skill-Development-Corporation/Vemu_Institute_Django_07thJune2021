from django.urls import path
from MyApp import views

urlpatterns = [
	path('demo/',views.demo,name='demo'),
	path('register/',views.register,name='register'),
	path('login/',views.login,name='login'),
]