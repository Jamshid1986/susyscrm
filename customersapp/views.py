from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse 
from django.http import HttpResponse
from django.views.generic import *
from .models import *
from .forms import *
from agentsapp.mixins import CompanyAndLoginRequiredMixin

# Create your views here.

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserForm

    def get_success_url(self):
        return reverse('customersapp:customers_list')

class HomeView(TemplateView):
    template_name = 'home.html'

class CustomersListView(LoginRequiredMixin, ListView):
    template_name = 'customers/customers_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        user = self.request.user
        if user.is_company:
            queryset = Customer.objects.all()
        else:
            queryset = Customer.objects.filter(company = user.agent.company)
            queryset = queryset.filter(agent_user = self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CustomersListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_company:
            queryset = Customer.objects.filter(
                company = user.userprofile,
                agent__isnull = True
            )
            context.update({
                "unassigned_customers":queryset
            })
        return context

class CustomerDetailView(CompanyAndLoginRequiredMixin, DetailView):
    template_name = 'customers/details.html'
    queryset = Customer.objects.all()
    context_object_name = 'customer'

class CustomerCreateView(CompanyAndLoginRequiredMixin, CreateView):
    template_name = 'customers/create_customer.html'
    form_class = CustomerModelForm

    def get_success_url(self):
        return reverse('customersapp:customers_list')

    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.company = self.request.user.userprofile
        customer.save()
        send_mail(
            subject = 'Bu mijoz yaratilgan',
            message = "Yangi mijoz qo'shing",
            from_email = "test@test.com",
            recipient_list = ["test2@test.com"],
        )

class CustomerUpdateView(CompanyAndLoginRequiredMixin, UpdateView):
    template_name = 'customers/update_customer.html'
    form_class = CustomerModelForm
    queryset = Customer.objects.all()
    context_object_name = 'customer'

    def get_success_url(self):
        return reverse('customersapp:customers_list')

class CustomerDeleteView(CompanyAndLoginRequiredMixin, DeleteView):
    template_name = 'customers/delete.html'
    form_class = CustomerModelForm
    queryset = Customer.objects.all()

    def get_success_url(self):
        return reverse('customersapp:customers_list')

class AgentAssignView(CompanyAndLoginRequiredMixin, FormView):
    template_name = 'customers/determine_agent.html'
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AgentAssignView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            'request':self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse('customersapp:customers_list')

    def form_valid(self, form):
        agent = form.cleaned_data['agent']
        customer = Customer.objects.get(id = self.kwargs['pk'])
        customer.agent = agent
        customer.save()
        return super(AgentAssignView, self).form_valid(form)

class CategoryListView(LoginRequiredMixin, ListView):
    template_name = "customers/category.html"
    context_object_name = 'categories'
    #queryset = models.Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_company:
            queryset = Customer.objects.filter(
                company = user.userprofile,
            )
        else:
            queryset = Category.objects.filter(
                company = user.agent.company
            )
        context.update({
                "unassigned_category_quantity":queryset.filter(category__isnull=True).count()
            })
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_company:
            queryset = Category.objects.filter(
                company = user.userprofile
                )
        else:
            queryset = Category.objects.filter(
                company = user.agent.company
                )
        return queryset

class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'customers/category_details.html'
    context_object_name = 'category'

    def get_queryset(self):
        user = self.request.user
        if user.is_company:
            queryset = Category.objects.filter(
                company = user.userprofile
                )
        else:
            queryset = Category.objects.filter(
                company = user.agent.company
                )
        return queryset

class CustomerCategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'customers/category_update_detail.html'
    form_class = CustomerCategoryUpdateForm
    def get_queryset(self):
        user = self.request.user
        if user.is_company:
            queryset = Customer.objects.filter(
                company = user.userprofile
            )
        else:
            queryset = Customer.objects.filter(
                company = user.agent.company
            )
        return queryset

    def get_success_url(self):
        return reverse('customersapp:customers_list')