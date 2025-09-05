from django.shortcuts import get_object_or_404, render

from grounds.models import Grounds

# Create your views here.

def grounds(request):
    ground = Grounds.objects.all()
    context = {
        'grounds':ground
    }
    return render(request,'grounds.html',context)

def ground_details(request,pk):
    ground_details = get_object_or_404(Grounds,pk = pk)
    context = {
        'ground_details' : ground_details
    }
    
    return render(request,'ground_detail.html',context)

