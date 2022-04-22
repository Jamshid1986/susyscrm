from django.urls import path
from .views import *

app_name = 'agentsapp'

urlpatterns = [
    path('', AgentListView.as_view(), name='agents'),
    path('create_agent/', AgentCreateView.as_view(), name='create_agent'),

]