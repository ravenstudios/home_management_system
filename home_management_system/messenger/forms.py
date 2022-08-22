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
    
    class Meta:
        model = Message
        fields = ["task_options", "comments"]



class CreateNewMessage(ModelForm):
    title = form.CharField()
    msg = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Message
        fields = ["title", "msg"]
