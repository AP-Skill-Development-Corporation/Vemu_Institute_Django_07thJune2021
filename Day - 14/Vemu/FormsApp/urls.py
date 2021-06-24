from django.urls import path
from FormsApp import views

urlpatterns = [
	path('demo/',views.demo),
	path('reg/',views.register,name='register'),
	path('details/',views.details,name='details'),
	path('update/<int:id>',views.update,name='update'),
	path('delete/<int:id>',views.delete,name='delete'),
]