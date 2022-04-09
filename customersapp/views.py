from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models
from .forms import *

# Create your views here.

def customers_list(request):
    customers = models.Customer.objects.all()

    context = {
        "customers": customers
    }
    return render(request, 'customers_list.html', context)

def customer_detail(request, pk):
    print(pk)
    customer = get_object_or_404(models.Customer, id=pk)
    
    context = {
        "customer":customer
    }
    print(customer)
    return render(request, 'details.html', context)


def create_customer(request):
    form = CustomerModelForm() # form = CustomerCreateForm -> CustomerModelForm()
    if request.method == "POST":
        print("Saved")
        form = CustomerModelForm(request.POST) # form = CustomerCreateForm -> CustomerModelForm()
        if form.is_valid():
            form.save()
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # age = form.cleaned_data['age']
            # agent = models.Agent.objects.first()
            # models.Customer.objects.create(
            #     first_name = first_name,
            #     last_name = last_name,
            #     age = age,
            #     agent = agent
            # )
            print("Success!")
            return redirect('/customers')
    context = {
        'forms': form
                }
    return render(request, "create_customer.html", context)


def customer_update(request, pk):
    print(pk)
    customer = Customer.objects.get(id=pk)
    
    context = {
        "customer":customer
    }
    print(customer)
    return render(request, 'update.html', context)


def update_customer(request, pk):
    customer = models.Customer.objects.get(id=pk)
    form = CustomerModelForm(instance=customer) # form = CustomerCreateForm -> CustomerModelForm()
    if request.method == "POST":
        print("Saved")
        form = CustomerModelForm(request.POST, instance=customer) # form = CustomerCreateForm -> CustomerModelForm()
        if form.is_valid():
            form.save()
            
            print("Success!")
            return redirect('/customers')
    context = {
        'customer': customer,
        'form': form
                }
    return render(request, "update_customer.html", context)