from django.db import models
from accounts.models import FamilyMember





class Chore(models.Model):
    assigned_to = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    # day = models.ForeignKey(Day, on_delete=models.CASCADE)
    chore_name = models.CharField(max_length=20, default="chore")
    note = models.TextField(max_length=80, blank=True, null=True)
    completed = models.BooleanField(default=False, null=True, blank=True)
    parents_completed = models.BooleanField(default=False, null=True, blank=True)
    repeated_chore = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    date_parent_completed = models.DateTimeField(blank=True, null=True)
    chore_status = models.CharField(max_length=20, default="pending")



    def __str__(self):
        return self.chore_name


class Day(models.Model):
    day_name = models.CharField(max_length=20, blank=True)
    chores = models.ManyToManyField(Chore, blank=True)



    def __str__(self):
        return self.day_name
