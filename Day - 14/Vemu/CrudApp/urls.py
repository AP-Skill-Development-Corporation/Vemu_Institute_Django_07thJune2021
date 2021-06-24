from django.urls import path
from CrudApp import views

urlpatterns = [
	path('demo/',views.demo,name = 'demo'),
	path('register/',views.register,name='register'),
	path('display/',views.display,name='display'),
	path('update/<int:id>/',views.update,name='update'),
	path('delete/<int:id>/',views.delete,name='delete'),
]