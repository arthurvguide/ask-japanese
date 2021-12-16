from .models import Booking
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
 
    class Meta:
        model = Booking  
        labels = {
        'full_name':'name',
        'booking_date': 'date',
        'booking_time': 'time'
        }
        fields = ('full_name', 'party_size','booking_date', 'booking_time', 'phone_number')
        widgets = {'booking_date': DateInput()}