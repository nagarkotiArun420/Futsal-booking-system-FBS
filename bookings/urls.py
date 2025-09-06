
from bookings import views
from django.urls import path


urlpatterns = [
    path('ground_details/<int:pk>/book/',views.booking, name = 'booking'),
    path('mybookings/', views.mybookings, name = "mybookings"),
]
