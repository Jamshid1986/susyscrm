from django.contrib import admin
from .models import Agent, Customer, User

# Register your models here.

admin.site.register(Customer)
admin.site.register(User)
admin.site.register(Agent)

