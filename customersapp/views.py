from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def home(request):
    customers = models.Customer.objects.all()

    context = {
        "customers": customers
    }
    return render(request, 'index.html', context)

