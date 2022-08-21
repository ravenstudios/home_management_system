from django.contrib import admin

# Register your models here.
from .models import UserProfile, FamilyMember

admin.site.register(UserProfile)
admin.site.register(FamilyMember)
