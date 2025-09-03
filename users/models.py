
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, blank = True)
    photo = models.ImageField(upload_to='images',blank = True, null = True)
    
    def __str__(self):
        return self.user.username
    
    