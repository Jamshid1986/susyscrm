import imp
from django import forms 
#from customersapp.models import Agent
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from customersapp.models import User

User = get_user_model()

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name'
        )
