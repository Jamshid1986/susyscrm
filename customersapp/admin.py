from django.contrib import admin
from .models import Agent, Customer, User, UserProfile, Category

# Register your models here.

admin.site.register(Customer)
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(UserProfile)
admin.site.register(Category)

