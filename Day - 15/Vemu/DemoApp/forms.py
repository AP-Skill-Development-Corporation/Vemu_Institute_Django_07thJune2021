from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserReg(UserCreationForm):
	password1 = forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control",'placeholder':'Enter password'}))
	password2 = forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control",'placeholder':'Enter password'}))
	class Meta:
		model = User
		fields = ['username']
		widgets = {
			'username':forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter username','requires':True,})
		}

class UpdateUserdetails(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),
			'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First name'}),
			'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last name'}),
			'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
			
		}