from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES=(('M','Male'),('F','Female'),('T','Transgender'))

class UserData(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=30)
	dob = models.DateField()
	location=models.CharField(max_length=30)

class customer(models.Model):
	First_name=models.CharField(max_length=30)
	Last_name=models.CharField(max_length=30)
	Email=models.EmailField()
	Date_Of_Birth=models.DateField()
	Age=models.IntegerField()
	Gender=models.CharField(choices=GENDER_CHOICES, max_length=30)

class newsletter(models.Model):
	Email=models.EmailField()
		