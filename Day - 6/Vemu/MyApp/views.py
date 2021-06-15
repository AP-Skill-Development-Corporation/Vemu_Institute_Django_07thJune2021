from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse('From demo App')

def register(request):
	return render(request,'MyApp/register.html')