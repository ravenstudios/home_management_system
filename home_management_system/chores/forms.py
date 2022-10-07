from django.forms import ModelForm
from .models import Chore
from django import forms
from django.forms.widgets import DateInput, NumberInput,CheckboxInput

class AddNewChore(ModelForm):

    class Meta:
        model = Chore
        compleated = forms.BooleanField(required=False, widget=forms.CheckboxInput)

        fields = "__all__"
