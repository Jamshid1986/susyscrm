from multiprocessing import context
from re import template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse 
from django.http import HttpResponse
from django.views.generic import TemplateView, DeleteView, ListView, DetailView, CreateView, UpdateView
from . import models
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
    template_name = 'customers_list.html'
    #queryset = models.Customer.objects.all()
    context_object_name = 'customers'

    def get_queryset(self):
        user = self.request.user
        if user.is_company:
            queryset = Customer.objects.filter(company = user.userprofile)
        else:
            queryset = Customer.objects.filter(company = user.agent.company)
            queryset = queryset.filter(agent_user = self.request.user)
        return queryset


# def customers_list(request):
#     customers = models.Customer.objects.all()

#     context = {
#         "customers": customers
#     }
#     return render(request, 'customers_list.html', context)

class CustomerDetailView(CompanyAndLoginRequiredMixin, DetailView):
    template_name = 'details.html'
    queryset = models.Customer.objects.all()
    context_object_name = 'customer'

# def customer_detail(request, pk):
#     #print(pk)
#     customer = get_object_or_404(models.Customer, id=pk)
    
#     context = {
#         "customer":customer
#     }
#     #print(customer)
#     return render(request, 'details.html', context)

class CustomerCreateView(CompanyAndLoginRequiredMixin, CreateView):
    template_name = 'customers/create_customer.html'
    form_class = CustomerModelForm

    def get_success_url(self):
        return reverse('customersapp:customers_list')



# def create_customer(request):
#     form = CustomerModelForm() # form = CustomerCreateForm -> CustomerModelForm()
#     if request.method == "POST":
#         print("Saved")
#         form = CustomerModelForm(request.POST) # form = CustomerCreateForm -> CustomerModelForm()
#         if form.is_valid():
#             form.save()
#             # first_name = form.cleaned_data['first_name']
#             # last_name = form.cleaned_data['last_name']
#             # age = form.cleaned_data['age']
#             # agent = models.Agent.objects.first()
#             # models.Customer.objects.create(
#             #     first_name = first_name,
#             #     last_name = last_name,
#             #     age = age,
#             #     agent = agent
#             # )
#             print("Success!")
#             return redirect('/customers')
#     context = {
#         'forms': form
#                 }
#     return render(request, "create_customer.html", context)

class CustomerUpdateView(CompanyAndLoginRequiredMixin, UpdateView):
    template_name = 'customers/update_customer.html'
    form_class = CustomerModelForm
    queryset = models.Customer.objects.all()
    context_object_name = 'customer'

    def get_success_url(self):
        return reverse('customersapp:customers_list')

# def customer_update(request, pk):
#     print(pk)
#     customer = Customer.objects.get(id=pk)
    
#     context = {
#         "customer":customer
#     }
#     print(customer)
#     return render(request, 'update.html', context)


# def update_customer(request, pk):
#     customer = models.Customer.objects.get(id=pk)
#     form = CustomerModelForm(instance=customer) # form = CustomerCreateForm -> CustomerModelForm()
#     if request.method == "POST":
#         print("Saved")
#         form = CustomerModelForm(request.POST, instance=customer) # form = CustomerCreateForm -> CustomerModelForm()
#         if form.is_valid():
#             form.save()
            
#             print("Success!")
#             return redirect('/customers')
#     context = {
#         'customer': customer,
#         'form': form
#                 }
#     return render(request, "update_customer.html", context)

class CustomerDeleteView(CompanyAndLoginRequiredMixin, DeleteView):
    template_name = 'customers/delete.html'
    form_class = CustomerModelForm
    queryset = models.Customer.objects.all()

    def get_success_url(self):
        return reverse('customersapp:customers_list')

# def delete_customer(request, pk):
#     customer = models.Customer.objects.get(id=pk)
#     customer.delete()
#     return redirect('/customers')