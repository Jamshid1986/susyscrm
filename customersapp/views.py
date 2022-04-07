from multiprocessing import context
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from . import models
# Create your views here.

def customers_list(request):
    customers = models.Customer.objects.all()

    context = {
        "customers": customers
    }
    return render(request, 'customers_list.html', context)

def customer_detail(request, pk):
    print(pk)
    customer = get_list_or_404(models.Customer, id=pk)
    
    context = {
        "customer":customer
    }
    print(customer)
    return render(request, 'details.html', context)

