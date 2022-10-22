from django.contrib import admin
from .models import Chore, ChoreLogs
# Register your models here.
admin.site.register(Chore)
admin.site.register(ChoreLogs)
