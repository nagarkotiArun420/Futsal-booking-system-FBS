
from django.urls import path
from . import views

urlpatterns = [
    path('grounds/', views.grounds, name='grounds')
]
