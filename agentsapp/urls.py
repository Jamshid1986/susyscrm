from django.urls import path
from .views import AgentListView

app_name = 'agentsapp'

urlpatterns = [
    path('', AgentListView.as_view(), name='agents')

]