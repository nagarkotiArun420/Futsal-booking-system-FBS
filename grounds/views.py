from django.shortcuts import render

from grounds.models import Grounds

# Create your views here.

def grounds(request):
    ground = Grounds.objects.all()
    context = {
        'grounds':ground
    }
    return render(request,'grounds.html',context)