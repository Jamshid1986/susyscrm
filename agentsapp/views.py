from re import template
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from customersapp.models import Agent
from .forms import AgentModelForm
from django.urls import reverse
# Create your views here.

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/agents_list.html'

    def get_queryset(self):
        #filterlash
        company = self.request.user.userprofile
        return Agent.objects.filter(company=company)


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/create_agent.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agentsapp:agents')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.profile = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


#sucrm-52 nomli arxivdan chiqarilib olindi.
class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_details.html"
    context_object_name = "agent"

    def get_queryset(self):
        return Agent.objects.filter(company=company)

class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "agents/update_agent.html"
    form_class = AgentModelForm

    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse("agentsapp:agents")

class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "agents/delete_agent.html"
    context_object_name = "agent"

    def get_queryset(self):
        return Agent.objects.filter(company=company)

    def get_success_url(self):
        return reverse("agentsapp:agents")