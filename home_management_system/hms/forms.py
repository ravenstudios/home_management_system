from django.forms import ModelForm
from django import forms
from messenger.models import Message
from django.forms.widgets import DateInput, NumberInput,CheckboxInput

TASK_OPTIONS = (
    ('Not Compleated','Not Compleated'),
    ('Compleated','Compleated'),
    ('Problem','Problem'),
    )


class UpdateTask(ModelForm):
    task_options = forms.ChoiceField(choices = TASK_OPTIONS)

    class Meta:
        model = Message
        fields = ["task_options"]
