from django.db import models
from accounts.models import FamilyMember



class Chore(models.Model):
    assigned_to = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    chore_name = models.CharField(max_length=20, default="chore")
    note = models.CharField(max_length=80, blank=True, null=True)
    completed = models.BooleanField(default=False, null=True, blank=True)
    partents_completed = models.BooleanField(default=False, null=True, blank=True)
    repeated_chore = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    date_completed = models.DateField(blank=True, null=True)
    date_patrent_completed = models.DateField(blank=True, null=True)



    def __str__(self):
        return self.chore_name


class Day(models.Model):
    day_name = models.CharField(max_length=20, blank=True)
    chores = models.ManyToManyField(Chore, blank=True)


    def __str__(self):
        return self.day_name
