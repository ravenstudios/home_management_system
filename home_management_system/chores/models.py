from django.db import models
from accounts.models import FamilyMember





class ChoreTemplate(models.Model):
    assigned_to = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    day_assigned = models.CharField(max_length=20, default="day")
    chore_name = models.CharField(max_length=100, default="chore")
    note = models.TextField(max_length=1000, blank=True, null=True)
    completed = models.BooleanField(default=False, null=True, blank=True)
    parents_completed = models.BooleanField(default=False, null=True, blank=True)
    repeated_chore = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    chore_start_time = models.DateTimeField(blank=True, null=True)
    chore_status = models.CharField(max_length=20, default="pending")

    class Meta:
        abstract = True


    def __str__(self):
        return self.chore_name



class Chore(ChoreTemplate):
    pass

class ChoreLogs(ChoreTemplate):
    pass
