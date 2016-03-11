from django import forms

class AjaxForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=100)
    drink = forms.CharField(label='Drink:', max_length=100)