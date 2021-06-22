from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def demo(request):
	return HttpResponse('From DemoApplication ....)')


def home(request):
	return render(request,'DemoApp/home.html')


def about(request):
	return render(request,'DemoApp/about.html')

def contact(request):
	return render(request,'DemoApp/contact.html')