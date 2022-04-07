from multiprocessing import context
from django.shortcuts import render, get_object_or_404
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
    form = CustomerCreateForm()
    if request.method == "POST":
        print("Saved")
        form = CustomerCreateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = models.Agent.objects.first()
            models.Customer.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                agent = agent
            )
            print("Success!")
    context = {
        'forms': form
                }
    return render(request, "create_customer.html", context)

