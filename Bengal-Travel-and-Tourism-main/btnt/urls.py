"""btnt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from btntapp import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',views.homepage),
    path('login/',LoginView.as_view()),
    path('customreg/',views.customreg),
    path('check/',views.check),
	path('home/',views.home),
	path('logoutview/',views.logoutview),
	path('sendmail/',views.sendmail),
    path('sendpmail/',views.sendpmail),
    path('feedback/',views.feedback),
    path('createcustomerrecord/',views.createcustomerrecord),
    path('showcustomers/',views.showcustomers),
    path('delete/<int:id>/',views.delete),
    path('editcustomer/<int:id>/',views.editcustomer),
    path('forgot_pass/',views.forgot_pass),
    path('otp_value/',views.otp_value),
    path('resetpassword/',views.reset_password),
    path('tour_packages/',views.tour_packages)
]
