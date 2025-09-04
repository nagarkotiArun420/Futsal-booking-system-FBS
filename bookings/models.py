from django.db import models
from django.contrib.auth.models import User

from grounds.models import Grounds  


STATUS_CHOICE = (
    ('pending','PENDING'),
    ('PAID','paid'),
    ('CANCELLED','cancelled'),
)

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ground = models.ForeignKey(Grounds, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=100, choices= STATUS_CHOICE, default='pending')
    prince = models.DecimalField(max_digits=8, decimal_places=2)
    booked_at  = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.user.username} {self.ground.ground_name}" 
    
    