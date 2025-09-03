from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from futsal_main.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


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
    if request.method == 'POST':
         form = AuthenticationForm(request, request.POST)
         if form.is_valid():
           
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')   
            else: 
                print(form.errors)         
    else:
        form = AuthenticationForm()
   
    return render(request, "login.html",{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('home')