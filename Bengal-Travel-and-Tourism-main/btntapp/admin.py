from django.contrib import admin
from btntapp.models import UserData
from btntapp.models import customer,newsletter

# Register your models here.

admin.site.register(UserData)
admin.site.register(customer)
admin.site.register(newsletter)