from dataclasses import fields
from django import forms
from .models import Customer


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent'
        )

class CustomerCreateForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField(min_value=16)
    agent = forms.CharField(max_length=50)
