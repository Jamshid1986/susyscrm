from django.urls import path
from .views import *

app_name = "customersapp"
urlpatterns = [
    #susyscrmprojectga yuboradigan url so'rovlarini shu yerda kutib olamiz: 127.0.0.1:8000/all/
    path('', customers_list),

    #susyscrmproject/urls.py dan kelgan 127.0.0.1:8000/customers/ so'rovlarga <pk> qo'shib, customers_details metodga yuboradi.
    path('<pk>/', customers_details)
    

]