from django.shortcuts import render,redirect
from django.http import HttpResponse
from CrudApp.models import Student

# Create your views here.
def demo(request):
	return HttpResponse('From CrudApp')

def register(request):
	if request.method == 'POST':
		na = request.POST.get('name')
		num = request.POST.get('rollnum')
		age = request.POST.get('age')
		mob = request.POST.get('mobile')
		em = request.POST.get('email')
		addr = request.POST.get('addr')
		Student.objects.create(name=na,rollnum=num,age=age,
			mobile=mob,email=em,address=addr)
		return redirect('/crud/display')
	return render(request,'CrudApp/register.html')

def display(request):
	data = Student.objects.all()
	return render(request,'CrudApp/details.html',{'data':data})

def update(request,id):
	data = Student.objects.get(id=id)
	if request.method == 'POST':
		data.name = request.POST['name']
		data.rollnum = request.POST['rollnum']
		data.age = request.POST['age']
		data.mobile = request.POST['mobile']
		data.email = request.POST['email']
		data.address = request.POST['addr']
		data.save()
		return redirect('/crud/display')
	return render(request,'CrudApp/update.html',{'data':data})