from django.urls import path
from .views import *

app_name = "customersapp"
urlpatterns = [
    #susyscrmprojectga yuboradigan url so'rovlarini shu yerda kutib olamiz: 127.0.0.1:8000/all/
    path('', CustomersListView.as_view(), name='customers_list'),
    #susyscrmproject/urls.py dan kelgan 127.0.0.1:8000/customers/id so'rovlarga <pk> qo'shib, customers_details metodga yuboradi.
    path('<int:pk>/', CustomerDetailView.as_view(), name = 'customer_details'),
    #127.0.0.1:8000/customers/create
    path('create/', CustomerCreateView.as_view(), name = 'create_customer' ),
    path('categories/', CategoryListView.as_view(), name = 'categories' ),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name = 'category_detail'),
    path('<int:pk>/update/', CustomerUpdateView.as_view(), name='update_customer'),
    path('<int:pk>/determine_agent/', AgentAssignView.as_view(), name='assign_agent'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='delete_customer')
    

]