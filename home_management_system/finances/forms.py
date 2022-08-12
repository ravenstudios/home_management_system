from django.forms import ModelForm
from .models import Bill, Paycheck
from django import forms
from django.forms.widgets import DateInput, NumberInput,CheckboxInput

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
    name = forms.CharField(required=False)
    ammount = forms.IntegerField(required=False)
    due_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Bill
        fields = ["name", "ammount", "due_date"]


class PayBill(ModelForm):
    # paid = forms.BooleanField()
    paid = forms.BooleanField(
                              required = False,
                              widget=forms.widgets.CheckboxInput(attrs={'onclick':'this.form.submit();'}),
                              help_text = "Pa",
                              )
    # paid = forms.BooleanField(widget=forms.CheckboxInput(attrs={'onclick':'this.form.submit();'}),required=False, label="Status")
    class Meta:
        model = Bill
        fields = ["paid"]
        # widgets = {
        #     'is_anything_required' : CheckboxInput(attrs={'class': 'required checkbox form-control'}),
        # }
