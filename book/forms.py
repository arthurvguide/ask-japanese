from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
 
    class Meta:
        model = Booking  
        labels = {'full_name': 'Full Name',
                  'booking_date_start': 'When',
                  'phone_number': 'Contact Number',
                  'party_size': 'Group Size'}

        fields = ('full_name', 'party_size',
                  'booking_date_start', 'phone_number')

