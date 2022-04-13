from re import template
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from customersapp.models import Agent
# Create your views here.

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/agents_list.html'


    def get_queryset(self):
        return Agent.objects.all()
