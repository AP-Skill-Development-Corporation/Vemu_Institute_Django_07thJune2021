from django.shortcuts import render,redirect
from django.http import HttpResponse
from DemoApp.forms import UserReg,UpdateUserdetails
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
			username = data.cleaned_data.get('username')
			messages.success(request,'hii {} you are successfully registered'.format(username))
			return redirect('/dapp/login')
	data = UserReg()
	return render(request,'DemoApp/register.html',{'data':data})

@login_required
def dashboard(request):
	return render(request,'DemoApp/dashboard.html')

@login_required
def mailsend(request):
	return render(request,'DemoApp/mailsend.html')

@login_required
def profile(request):
	return render(request,'DemoApp/profile.html')

@login_required
def update(request):
	if request.method == 'POST':
		data = UpdateUserdetails(request.POST,instance=request.user)
		if data.is_valid():
			data.save()
			return redirect('/dapp/profile')
	data = UpdateUserdetails(instance = request.user)
	return render(request,'DemoApp/update.html',{'data':data})
