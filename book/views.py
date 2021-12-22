from django.shortcuts import render, get_object_or_404
from datetime import datetime, date, timedelta, time
from django.contrib import messages
from django.views import View
from .forms import BookingForm, CancelForm
from .models import Booking, Table
# Create your views here.

class BookingView(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'book.html', {
                'form': BookingForm()
                
            } 
        )

    def post(self, request, *args, **kwargs):

        minutes_slot = 90
        delta = timedelta(minutes=minutes_slot)

        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)

            #Getting input date to check if is there's table available
            required_size = booking.party_size 
            required_start_time = booking.booking_date_start 
            numbers_booked = avoid_double_booking(required_start_time)
            table = get_right_table_available(required_start_time, required_size)

            #Explaining for user that there's no table available at the required time
            if table == "No Table available":
                messages.warning(request, 'Sorry, there is no table available at this time, please try another date')
                return render(
                    request,
                    'book.html', {
                    'form': booking_form})

            #Explaining for user that they cant double book       
            if booking.phone_number in numbers_booked:
                messages.warning(request, 'You already has a booking at this time')
                return render(
                    request,
                    'book.html', {
                    'form': booking_form})

            #Passing booking end date to the Booking Model
            booking.booking_date_end = required_start_time + delta
            #Passing the table found to the Booking Model
            booking.table = table 
            booking.save()
            return render(request, 'book.success.html', {
                          'name': booking.full_name,
                          'group': booking.party_size,
                          'date': booking.booking_date_start,
                          'contact_number': booking.phone_number,
                          'id': booking.id
            })

        else:
            return render(
                    request,
                    'book.html', {
                    'form': booking_form})    


class CancelView(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'book.cancel.html', {
                'form': CancelForm()
            }
        )


def get_right_table_available(required_start_time, required_size):
    """
    This method returns the smallest table available of the restaurant.
    Checks if the table has enough size for the party size.
    Checks if the is being used at the required booking time.
    Each booking has 90 minutes.
    """
   
    delta = timedelta(minutes=90) # 90 min beacuse each bookins has 90min
    required_end_time = required_start_time + delta

    start_date = required_start_time
    end_date = required_end_time

    tables_booked_ids = []

    # Exclude tables which starts between the required booking time
    tables_booked = Booking.objects.filter(
        booking_date_start__range=(start_date, end_date)).values('table')
    tables_booked_ids_temp = [x['table'] for x in tables_booked]
    tables_booked_ids = tables_booked_ids + tables_booked_ids_temp

    # Exclude tables which ends between the required booking time
    tables_booked = Booking.objects.filter(
        booking_date_end__range=(start_date, end_date)).values('table')
    tables_booked_ids_temp = [x['table'] for x in tables_booked]
    tables_booked_ids = tables_booked_ids + tables_booked_ids_temp

    tables = Table.objects.filter(
        size__gte=required_size).exclude(id__in=tables_booked_ids).order_by('size')

    if tables.count() == 0:
        return "No Table available"
    else:
        return tables[0]


def avoid_double_booking(required_start_time):
    """
    This method returns all numbers of the bookings made at
    the range of start and end time of the new booking.
    This avoid of the same person make double booking.
    """
    delta = timedelta(minutes=90) # 90 min beacuse each bookins has 90min
    required_end_time = required_start_time + delta

    start_date = required_start_time
    end_date = required_end_time

    all_numbers_booked = []

    # Get numbers which starts between the required booking time
    numbers_booked = Booking.objects.filter(
         booking_date_start__range=(start_date, end_date)).values('phone_number') 
    all_numbers_booked_temp = [x['phone_number'] for x in numbers_booked]
    all_numbers_booked = all_numbers_booked + all_numbers_booked_temp

    # Get numbers which ends between the required booking time
    numbers_booked = Booking.objects.filter(
         booking_date_end__range=(start_date, end_date)).values('phone_number')
    all_numbers_booked_temp = [x['phone_number'] for x in numbers_booked]
    all_numbers_booked = all_numbers_booked + all_numbers_booked_temp

    return all_numbers_booked