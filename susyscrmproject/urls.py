"""susyscrmproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView
)
from customersapp.views import HomeView, SignUpView

urlpatterns = [
    #customersapp dan keladigan url so'rovlarini shu yerda kutib olamiz: 127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),

    #path ichidagi 'customers/' direktoriyasi customers_list.html ichidagi href="/customers/" dan kelgan so'rovlarni qabul qilib,
    #customersapp/urls.py ga uzatadi.
    path('customers/', include('customersapp.urls', namespace='customersapp')),
    path('agents/', include('agentsapp.urls', namespace='agentsapp')),
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_reset/', PasswordResetView.as_view(), name='reset_password'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm')
]
