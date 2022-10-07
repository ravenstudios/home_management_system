from django.db import models
from accounts.models import FamilyMember

class Chore(models.Model):
    name = models.CharField(max_length=20, default="chore")
    note = models.CharField(max_length=20, blank=True)
    compleated = models.BooleanField(default=False)

    def __str__(self):
        return self.name
