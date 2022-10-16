from django.forms import ModelForm
from .models import Chore
from django import forms
from django.forms.widgets import DateInput, NumberInput,CheckboxInput
from accounts.models import FamilyMember

class AddNewChore(ModelForm):

    class Meta:
        model = Chore
        fields = ["chore_name", "note", "repeated_chore"]

        widgets = {"note": forms.Textarea}

class CompleteChore(ModelForm):


    class Meta:
        model = Chore
        fields = ["note", "completed", "parents_completed"]

        widgets = {"note": forms.Textarea}
