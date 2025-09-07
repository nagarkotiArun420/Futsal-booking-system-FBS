from django.shortcuts import get_object_or_404, render,redirect
from bookings.models import Book
from futsal_main.forms import BookingForm
from grounds.models import Grounds
from datetime import datetime, date
from decimal import Decimal
from django.contrib.auth.decorators import login_required

# Create your views here.

def booking(request,pk):
    ground = get_object_or_404(Grounds,pk=pk)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.ground = ground
            booking.status = 'pending'
            
            # calculate the price
            start_time = booking.start_time
            end_time = booking.end_time
            
            start_dt = datetime.combine(date.today(), start_time)
            end_dt = datetime.combine(date.today(), end_time)
            
            duration = end_dt - start_dt
            hours = Decimal (duration.total_seconds() / 3600)
            total_price = ground.price_per_hour * hours
            booking.price = total_price
            form.save()       
            booking.save()
            return redirect('home')
        else:
            print(form.errors)
            
    else:
        form = BookingForm()
    context = {
        'form':form,
        'ground':ground
    }
    return render(request,'booking.html',context)


@login_required(login_url = 'login')

def mybookings(request):
    
    mybookings = Book.objects.filter(user = request.user)
    context = {
        'mybookings':mybookings,
        
    }
    
    return render(request,"mybookings.html",context)


    
def cancel_booking(request, pk):
    cancel_booking = get_object_or_404(Book,pk=pk)
    cancel_booking.delete()
    return redirect('home')
