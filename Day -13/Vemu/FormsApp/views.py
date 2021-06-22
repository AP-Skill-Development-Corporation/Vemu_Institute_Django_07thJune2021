from django.shortcuts import render,redirect
from django.http import HttpResponse
from FormsApp.models import Register
from FormsApp.forms import Reg

# Create your views here.
def demo(request):
	return HttpResponse('From FormsApp')

def register(request):
	if request.method == 'POST':
		formdata = Reg(request.POST)
		if formdata.is_valid():
			formdata.save()
			return redirect('/form/reg')
	formdata = Reg()
	return render(request,'FormsApp/register.html',{'data':formdata})

def details(request):
	data = Register.objects.all()
	return render(request,'FormsApp/details.html',{'data':data})

def update(request,id):
	a = Register.objects.get(id=id)
	if request.method == 'POST':
		u = Reg(request.POST,instance=a)
		if u.is_valid():
			u.save()
			return redirect('/form/details')
	u = Reg(instance=a)
	return render(request,'FormsApp/update.html',{'u':u})

def delete(request,id):
	d = Register.objects.get(id=id)
	if request.method == 'POST':
		d.delete()
		return redirect('/form/details')
	return render(request,'FormsApp/delete.html',{'d':d})