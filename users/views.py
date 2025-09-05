from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from futsal_main.forms import RegistrationForm,ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from grounds.models import Grounds



# Create your views here.
def home(request):
    featured_post = Grounds.objects.filter(is_featured  = True) #.first() can be used to show only one featured post
    grounds = Grounds.objects.all()
    
    return render(request,"home.html",{'featured_post':featured_post,'grounds':grounds})

def register(request):
    
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            messages.success(request, "Registration complete")
            return redirect('login')
    else:
        user_form = RegistrationForm()
        profile_form  = ProfileForm()
         
    context={
        'user_form':user_form,
        'profile_form':profile_form
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


@login_required(login_url= 'login' )
def profile(request):
    user = request.user
    profile = user.profile#Get the details of  using (request.user)
    context={
        'user':user,
        'profile':profile
    }
    return render(request,"userprofile.html",context)

def aboutus(request):
    return render(request,'aboutus.html')