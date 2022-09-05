from django.forms import ModelForm
from .models import Message
from django import forms
from django.forms.widgets import DateInput, NumberInput,CheckboxInput
from django.utils import timezone as tz
from django.db import models
from accounts.models import FamilyMember

TASK_OPTIONS = (
    ('Not Compleated','Not Compleated'),
    ('Compleated','Compleated'),
    ('Problem','Problem'),
    )



class UpdateMessage(ModelForm):
    task_options = forms.ChoiceField(choices = TASK_OPTIONS)
    comments = forms.CharField(required=False)
    time_updated = models.DateTimeField(db_column='time_updated',  default=tz.now)
    msg_author = forms.ModelChoiceField(queryset=FamilyMember.objects.all())
    class Meta:
        model = Message
        fields = ["task_options", "comments", "msg_author"]



class CreateNewMessage(ModelForm):
    title = forms.CharField()
    msg = forms.CharField(widget=forms.Textarea)
    # msg_author= forms.CharField(label='msg_author', widget=forms.Select())
    msg_author = forms.ModelChoiceField(queryset=FamilyMember.objects.all())
    msg_recipient = forms.ModelChoiceField(queryset=FamilyMember.objects.all())
    class Meta:
        model = Message
        fields = ["title", "msg", "msg_author", "msg_recipient"]


# class Message(models.Model):
#     title = models.CharField(max_length=200, default="TITLE")
#     msg = models.CharField(max_length=200, default="MESSAGE", blank=True)
#     msg_author = models.ForeignKey(FamilyMember, related_name="msg_author", on_delete=models.CASCADE, null=True)
#     msg_recipient = models.ForeignKey(FamilyMember, related_name="msg_recipient", on_delete=models.CASCADE, null=True)
#     task_options = models.CharField(max_length=20, choices=TASK_OPTIONS, default='Not Compleated')
#     time_created = models.DateTimeField(default=datetime.now, blank=True)
#     time_updated = models.DateTimeField(auto_now=True)
#     comments = models.CharField(max_length=300, default="Comments")
#     def __str__(self):
#         return self.title
