from btntapp.models import UserData
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from btntapp.models import customer

GENDER_CHOICES=(('M','Male'),('F','Female'),('T','Transgender'))

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'email','password1','password2')

class RegForm(forms.ModelForm):
	dob=forms.DateField(label='Date of Birth')
	gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
	class Meta:
		model=UserData
		fields=('bio','gender','dob','location')

class customerForm(forms.ModelForm):
	class Meta:
		model=customer
		fields="__all__"