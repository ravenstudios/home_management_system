from django.contrib import admin

# Register your models here.
from .models import Paycheck, Bill

admin.site.register(Paycheck)
admin.site.register(Bill)
