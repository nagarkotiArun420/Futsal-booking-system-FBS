from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bookings.models import Book
from users.models import Profile,Contact


class RegistrationForm(UserCreationForm):
     
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
        


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone','photo','address')
        
class BookingForm (forms.ModelForm):
    class Meta:
        model = Book
        fields = ('date','start_time','end_time')
        

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    
