from django.forms import ModelForm
from .models import Bill, Paycheck
from django import forms
from django.forms.widgets import DateInput, NumberInput

class CreateNewBill(ModelForm):
    name = forms.CharField(required=False)
    ammount = forms.IntegerField(required=False)
    due_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Bill
        fields = ["name", "ammount", "due_date"]



class CreateNewPaycheck(ModelForm):
    name = forms.CharField(required=False)
    ammount = forms.IntegerField(required=False)
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Paycheck
        fields = ["name", "ammount", "date"]


class UpdateMoneyInBank(ModelForm):
    ammount_in_bank = forms.IntegerField(label="XAmmount in bank")
    class Meta:
        model = Paycheck
        fields = ["ammount_in_bank"]



class UpdateBill(ModelForm):
    ammount = forms.DecimalField(label="Ammount", max_digits=6, decimal_places=2)
    class Meta:
        model = Bill
        fields = ["ammount"]
