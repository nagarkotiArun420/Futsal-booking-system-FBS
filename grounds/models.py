from django.db import models

# Create your models here.

class Grounds(models.Model):
    ground_name = models.CharField(max_length=60, null=False)
    location_name = models.CharField(max_length=100, blank=False, null=False)
    size = models.CharField(max_length=40)
    price_per_hour = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='ground/',null = True)
    
    class Meta:
        verbose_name_plural = 'Grounds'
    
    def __str__(self):
        return self.ground_name
    

    
    
    