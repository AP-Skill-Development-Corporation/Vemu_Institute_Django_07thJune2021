from django.db import models

# Create your models here.

class Register(models.Model):
	genders = [('Female','Female'),
				('Male','Male'),
				('Others','Others')]
	branchs = [('Select','Select'),('ECE','ECE'),('CSE','CSE'),
				('MEC','MEC'),('IT','IT'),('CIVIL','CIVIL')]
	name = models.CharField(max_length=20)
	mobile_no = models.CharField(max_length=10)
	age = models.IntegerField()
	gender = models.CharField(max_length=10,choices=genders,null=True)
	branch = models.CharField(max_length=10,choices=branchs,null=True)
