from django.forms import ModelForm
from .models import Item, List
from django import forms
from django.forms.widgets import DateInput, NumberInput,CheckboxInput

class CreateNewItem(ModelForm):
    name = forms.CharField()
    note = forms.CharField()
    class Meta:
        model = Item
        fields = ["name", "note"]

class CreateNewList(ModelForm):
    name = forms.CharField()
    note = forms.CharField()
    class Meta:
        model = List
        fields = ["name", "note"]
