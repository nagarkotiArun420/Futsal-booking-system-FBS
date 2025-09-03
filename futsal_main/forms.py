from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    
    phone = forms.CharField(max_length = 15)
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','phone','password1','password2')
    
