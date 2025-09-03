from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile


class RegistrationForm(UserCreationForm):
     
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
        


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone','photo')
        
    
