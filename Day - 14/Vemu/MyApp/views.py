from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse('From demo App')

def register(request):
	if request.method == "POST":
		name = request.POST['uname']
		email = request.POST['email']
		mobile = request.POST['mobile']
		gender = request.POST['optradio']
		dob = request.POST['dob']
		lang = request.POST.getlist('lan')
		filename = request.POST['file']
		#print(name,email,mobile,gender,dob,lang,filename)
		return render(request,'MyApp/details.html',{'uname':name,'mail':email,'mob':mobile,
			'gender':gender,'dateofbirth':dob,'languagues':lang,'fname':filename})
	return render(request,'MyApp/register.html')


def login(request):
	if request.method == 'POST':
		u = request.POST['uname']
		p = request.POST['pswd']
		#print(u,p)
		#return HttpResponse("Hii.. your username is : {}".format(u))
		if u == 'Apssdc' and p == 'Apssdc123':
			return HttpResponse("<h2>Hii.. welcome {}</h2>".format(u))
		else:
			return HttpResponse("<h2>Invalid details....)</h2>")
	return render(request,'MyApp/login.html')