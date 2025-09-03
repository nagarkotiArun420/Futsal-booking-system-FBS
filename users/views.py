from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from futsal_main.forms import RegistrationForm


# Create your views here.
def home(request):
    return render(request,"home.html")

def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm() 
    context={
        'form':form
    }  
    
    return render(request,"register.html",context)

def login(request):
    
    return render(request, "login.html")