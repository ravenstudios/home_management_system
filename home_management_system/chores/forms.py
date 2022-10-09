from django.forms import ModelForm
from .models import Chore
from django import forms
from django.forms.widgets import DateInput, NumberInput,CheckboxInput
from accounts.models import FamilyMember

class AddNewChore(ModelForm):
    # assigned_to = forms.ModelChoiceField(queryset=FamilyMember.objects.all())


    class Meta:
        model = Chore



        fields = ["assigned_to", "chore_name", "note"]



class CompleteChore(ModelForm):

    class Meta:
        model = Chore

        fields = ["note", "completed", "partents_completed"]
