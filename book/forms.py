from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
 
    class Meta:
        model = Booking  

        fields = ('full_name', 'party_size',
                  'booking_date_start', 'phone_number')

