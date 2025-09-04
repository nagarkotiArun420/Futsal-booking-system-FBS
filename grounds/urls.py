
from django.urls import path
from . import views

urlpatterns = [
    path('grounds/', views.grounds, name='grounds'),
    path('ground_details/<int:pk>/',views.ground_details, name = 'ground_details')
]
