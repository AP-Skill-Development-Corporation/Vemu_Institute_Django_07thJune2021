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

def basic(request,num):
	return HttpResponse('My roll number is:{}'.format(num))

def task(request,name,id):
	return HttpResponse("My name is {} and my roll number is {}".format(name,id))

def temp(request):
	return render(request,'myApp/temp.html')

def ls(request,name,id):
	return render(request,'myApp/ls.html',{'n':name,'i':id})

def table(request):
	return render(request,'myApp/table.html')

def inline(request):
	return render(request,'myApp/inline.html')

def internal(request):
	return render(request,'myApp/internal.html')

def external(request):
	return render(request,'myApp/external.html')

