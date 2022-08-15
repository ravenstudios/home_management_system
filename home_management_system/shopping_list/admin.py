from django.contrib import admin

# Register your models here.
from .models import Item, List

admin.site.register(Item)
admin.site.register(List)
