
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, blank = True)
    photo = models.ImageField(upload_to='avatar/',blank = True, null = True)
    address = models.CharField(max_length=50, blank=True, null= True)
    
    def __str__(self):
        return self.user.username
    

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=255, blank=True, null=True)
    Message = models. TextField(max_length=1000)
    phone = models.CharField(max_length=15, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        
    
    
    
    
    