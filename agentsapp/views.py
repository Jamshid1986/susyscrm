from email import message
from re import template
from django.shortcuts import render
from django.views import generic
from .mixins import CompanyAndLoginRequiredMixin
from customersapp.models import Agent
from .forms import AgentModelForm
from django.urls import reverse
import random
from django.core.mail import send_mail
# Create your views here.

class AgentListView(CompanyAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agents_list.html'

    def get_queryset(self):
        #filterlash
        company = self.request.user.userprofile
        return Agent.objects.filter(company=company)


class AgentCreateView(CompanyAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/create_agent.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agentsapp:agents')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_company = False
        user.is_agent = True
        user.set_password(f"{random.randint(0,1000)}")
        #agent.profile = self.request.user.userprofile
        user.save()
        Agent.objects.create(
            user = user,
            company = self.request.user.userprofile
        )
        send_mail(
            subject = "Bu Agent yaratilgan",
            message = "Yangi Agent yaratilgan",
            from_email = "jimamaliyev@gmail.com",
            recipient_list=[user.email],
        )
        return super(AgentCreateView, self).form_valid(form)


#sucrm-52 nomli arxivdan chiqarilib olindi.
class AgentDetailView(CompanyAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_details.html"
    context_object_name = "agent"

    def get_queryset(self):
        return Agent.objects.filter(company=company)

class AgentUpdateView(CompanyAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/update_agent.html"
    form_class = AgentModelForm

    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse("agentsapp:agents")

class AgentDeleteView(CompanyAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/delete_agent.html"
    context_object_name = "agent"

    def get_queryset(self):
        return Agent.objects.filter(company=company)

    def get_success_url(self):
        return reverse("agentsapp:agents")