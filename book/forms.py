from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
 
    class Meta:
        model = Booking  
        labels = {'full_name': 'name',
                  'booking_date_start': 'when'}

        fields = ('full_name', 'party_size',
                  'booking_date_start', 'phone_number')
