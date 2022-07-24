from django.forms import ModelForm
from .models import Bill, Paycheck
from django import forms

class CreateNewBill(ModelForm):
    name = forms.CharField()
    ammount = forms.IntegerField()
    due_date = forms.IntegerField()

    class Meta:
        model = Bill
        fields = ["name", "ammount", "due_date"]


class CreateNewPaycheck(ModelForm):
    name = forms.CharField()
    ammount = forms.IntegerField()
    date = forms.IntegerField()

    class Meta:
        model = Paycheck
        fields = ["name", "ammount", "date"]
