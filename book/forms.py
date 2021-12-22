from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
 
    class Meta:
        model = Booking  

        fields = ('full_name', 'party_size',
                  'booking_date_start', 'phone_number')


class CancelForm(forms.Form):

    your_name = forms.CharField(required=True, max_length=50)
    your_booking_id = forms.IntegerField(required=True)