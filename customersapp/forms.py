from dataclasses import fields
from urllib import request
from django import forms
from .models import Agent, Customer, User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()
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
    first_name = forms.CharField(max_length=20,)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField(min_value=16)
    agent = forms.CharField(max_length=50)

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}

class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        agents = Agent.objects.filter(company=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset=agents

class CustomerCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'category',
        )