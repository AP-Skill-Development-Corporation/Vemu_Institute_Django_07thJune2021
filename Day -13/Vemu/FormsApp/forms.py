from django import forms
from django.forms import ModelForm
from FormsApp.models import Register


class Reg(forms.ModelForm):
	class Meta:
		model = Register
		fields = ['name','mobile_no','age','gender','branch']
		widgets = {
			'name':forms.TextInput(attrs= {'class':'form-control','placeholder':'Enter name'}),
			'mobile_no':forms.TextInput(attrs= {'class':'form-control','placeholder':'Enter Mobile number'}),
			'age':forms.NumberInput(attrs= {'class':'form-control','placeholder':'Enter age'}),
			'gender':forms.RadioSelect(attrs= {'type':'radio','placeholder':'Select Gender'}),
			'branch':forms.Select(attrs= {'class':'form-control'}),

		}