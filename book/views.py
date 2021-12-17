from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Table
from .forms import BookingForm
# Create your views here.

class Booking(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'book.html', {
                'form': BookingForm()
            } 
        )

    def post(self, request, *args, **kwargs):

        table = get_object_or_404(Table, pk=22)
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.table = table 
            booking.save()
        else :
            return render(
                request,
                'book.html', {
                    'form': booking_form
                } 
            )    
        
        return render(request, 'index.html')