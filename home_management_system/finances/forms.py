from django import forms

class create_new_bill(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
