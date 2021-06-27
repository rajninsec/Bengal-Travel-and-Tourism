from django.shortcuts import render,redirect
from btntapp.form import UserForm,RegForm,customerForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from btnt import settings
from btntapp.models import customer,newsletter
from django.contrib.auth.models import User
import random

# Create your views here.

def homepage(request):
	return render(request,"index.html")

def customreg(request):
	if request.method=="POST":
		user=UserForm(request.POST)
		form=RegForm(request.POST)
		if user.is_valid() and form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			user.save()
			profile.save()
			return redirect("/login/")
	else:
		user=UserForm()
		form=RegForm()
	return render(request,"registration/customreg.html",{'form':form,'user':user})

def check(request):
	username=request.POST['username']
	password=request.POST['password']
	user=authenticate(request,username=username,password=password)
	if user is not None:
		login(request,user)	#logs in the user
		return redirect("/home")
	else:
		return redirect("/login")

@login_required
def home(request):
	username=request.user.first_name
	return render(request,"home.html",{'first_name':username})

def logoutview(request):
	logout(request)#logsout the current user
	return redirect("/login")

def sendmail(request):
	if request.method=="POST":
	     subject = "Greetings from Bengal Travel and Tourism"
	     msg = "Congratulations your email has been registered with us. We will inform you when we have latest offers"
	     to = request.POST['E-mail']
	     emails = newsletter.objects.values_list('Email', flat=True)
	     if to not in emails:
	     	newsletter(Email=to).save()
	     res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
	     if(res == 1):
	          msg = "Mail sent successfully"
	     else:
	          msg = "Mail could not be sent"
	     return HttpResponse(msg)
	else:
		return render(request,'index.html')

def sendpmail(request):
	if request.method=="POST":
	     subject = "Greetings from Bengal Travel and Tourism"
	     name = request.POST['Name']
	     msg = request.POST['msg']
	     to = request.POST['Email']
	     emails = newsletter.objects.values_list('Email', flat=True)
	     if to not in emails:
	     	newsletter(Email=to).save()
	     res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
	     if(res == 1):
	          msg = "Mail sent successfully to "+name
	     else:
	          msg = "Mail could not be sent"
	     return HttpResponse(msg)
	else:
		return render(request,'index.html')

def feedback(request):
	if request.method=="POST":
		name = request.POST['opus']
		to = request.POST['email']
		emails = newsletter.objects.values_list('Email', flat=True)
		if to not in emails:
			newsletter(Email=to).save()
		subject = request.POST['opu']
		msg = request.POST['op']
		res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to,'kundankumardec16@gmail.com'])
		if(res == 1):
			msg = "Thanks Mr."+name+" for your compliment. We have also sent a copy of your suggestion to "+to
		else:
			msg = "Mail could not be sent"
		return HttpResponse(msg)
	else:
		return render(request,'index.html')

def createcustomerrecord(request):
	if request.method=="POST":
		form=customerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/showcustomers")
	else:
		form=customerForm()
		return render(request,"createcustomerrecord.html",{'form':form})

def showcustomers(request):
	customers=customer.objects.all()
	return render(request,"showcustomers.html",{'customers':customers})

def delete(request,id):
	customers=customer.objects.get(id=id)
	customers.delete()
	return redirect("/showcustomers/")

def editcustomer(request,id):
	customers=customer.objects.get(id=id)
	if request.method=="POST":
		form=customerForm(request.POST,instance=customers)
		if form.is_valid():
			form.save()
			return redirect('/showcustomers/')
	else:
		form=customerForm()
		return render(request,"editcustomer.html",{'form':form,'customers':customers})

def forgot_pass(request):
	if request.method=="POST":
		username=request.POST['username']
		check = User.objects.filter(is_active=True).values_list('username', flat=True)
		if username in check:
			person = User.objects.get(username=username)
			key=random.randint(1000000,9999999)
			to=person.email
			subject="Bengal Travel and Tourism"
			msg="Your OTP for "+to+" is "+str(key)
			res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
			if(res == 1):
				request.session["otp"]=str(key)
				request.session["username"]=username
				return redirect("/otp_value")
			else:
				return HttpResponse("<center><b><br><br><br><br><br><br><br><br><br><br><br><br><br><h2>Mail could not be sent. Please try after sometime.</h2></b></center>")
		else:
			return HttpResponse("<center><b><br><br><br><br><br><br><br><br><br><br><br><br><br><h2>Username doesn't exist in our record.</h2></b></center>")  
	else:
		return render(request,'forgot_pass.html')

def otp_value(request):
	if request.method=="POST":
		otp=request.POST['otp_value']
		if (otp==request.session["otp"]):
			del request.session["otp"]
			return redirect('/resetpassword')
		else:
			return HttpResponse("<center><b><br><br><br><br><br><br><br><br><br><br><br><br><br><h2>Your OTP doesn't match.</h2></b></center>")
	else:
		return render(request,'otp_value.html')

def reset_password(request):
	if request.method=="POST":
		pass1=request.POST['for_reset_pass1']
		pass2=request.POST['for_reset_pass2']
		if(pass1==pass2):
			u = User.objects.get(username=request.session["username"])
			u.set_password(pass2)
			u.save()
			del request.session["username"]
			subject="Bengal Travel and Tourism"
			msg="Your password has been changed successfully"
			to=u.email
			res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
			return redirect('/login/')
		else:
			return HttpResponse("<center><b><br><br><br><br><br><br><br><br><br><br><br><br><br><h2>Your password doesn't match.</h2></b></center>")
	return render(request,'resetpassword.html')

def tour_packages(request):
	return render(request,'tour_packages.html')
