from django.shortcuts import render,redirect
from django.http import HttpResponse
from DemoApp.forms import UserReg
# Create your views here.

def demo(request):
	return HttpResponse('From DemoApplication ....)')


def home(request):
	return render(request,'DemoApp/home.html')


def about(request):
	return render(request,'DemoApp/about.html')

def contact(request):
	return render(request,'DemoApp/contact.html')

def register(request):
	if request.method == 'POST':
		data = UserReg(request.POST)
		if data.is_valid():
			data.save()
			return redirect('/dapp/login')
	data = UserReg()
	return render(request,'DemoApp/register.html',{'data':data})







