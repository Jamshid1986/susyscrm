from django import forms

class CustomerCreateForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField(min_value=16)
    agent = forms.CharField(max_length=50)
