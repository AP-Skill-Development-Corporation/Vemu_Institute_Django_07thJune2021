from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hai(request):
	return HttpResponse("hai guys welcome to Django session")

def hello(request):
	return HttpResponse("<h3 style=color:skyblue;background-color:red;font-size:20px>welcom to session</h3>")

def sample(request):
	n="apssdc"
	return HttpResponse("welcome to" +n)

def hm(request,name):
	return HttpResponse('My name is:{}'.format(name))