from django.db import models
from accounts.models import FamilyMember
from datetime import datetime



TASK_OPTIONS = (
    ('Not Compleated','Not Compleated'),
    ('Compleated','Compleated'),
    ('Problem','Problem'),
    )



# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=200, default="TITLE")
    msg = models.CharField(max_length=200, default="MESSAGE", blank=True)
    msg_author = models.ForeignKey(FamilyMember, related_name="msg_author", on_delete=models.CASCADE, null=True)
    msg_recipient = models.ForeignKey(FamilyMember, related_name="msg_recipient", on_delete=models.CASCADE, null=True)
    task_options = models.CharField(max_length=20, choices=TASK_OPTIONS, default='Not Compleated')
    time_created = models.DateTimeField(default=datetime.now, blank=True)
    time_updated = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=300, default="Comments")
    def __str__(self):
        return self.title
