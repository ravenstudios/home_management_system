from django.forms import ModelForm
from .models import Item, List
from django import forms
from django.forms.widgets import DateInput, NumberInput,CheckboxInput

class CreateNewItem(ModelForm):
    name = forms.CharField()
    note = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Item
        fields = ["name", "note", "date"]

class CreateNewList(ModelForm):
    name = forms.CharField()
    note = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = List
        fields = ["name", "note", "date"]
