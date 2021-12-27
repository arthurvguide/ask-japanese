from datetime import timedelta
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views import View
from .forms import BookingForm, FindBookingForm
from .models import Booking, Table


class BookingView(View):
    """
    This view is to the user make a booking
    at the restaurant
    """
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

            # Getting input date to check if is there's table available
            required_size = booking.party_size
            required_start_time = booking.booking_date_start
            numbers_booked = avoid_double_booking(required_start_time)
            table = get_right_table_available(required_start_time,
                                              required_size)

            # Explaining for user that there's no table available
            #  at the required time
            if table == "No Table available":
                messages.warning(request, 'Sorry, there is no table'
                                          ' available at this time,'
                                          ' please try another date')
                return render(request, 'book.html', {'form': booking_form})

            # Explaining for user that they cant double book
            if booking.phone_number in numbers_booked:
                messages.warning(request, 'You already has'
                                          ' a booking at this time')
                return render(request, 'book.html', {'form': booking_form})

            # Passing booking end date to the Booking Model
            booking.booking_date_end = required_start_time + delta
            # Passing the table found to the Booking Model
            booking.table = table
            booking.save()
            # Send an email to user save their booking details
            message = email_message(booking.full_name,
                                    booking.booking_date_start,
                                    booking.id)
            send_mail("Booking Confirmation",
                      message, settings.EMAIL_HOST_USER, [booking.email],
                      fail_silently=False)
            return render(request, 'book.success.html', {
                          'name': booking.full_name,
                          'group': booking.party_size,
                          'date': booking.booking_date_start,
                          'contact_number': booking.phone_number,
                          'email': booking.email,
                          'id': booking.id
                          })

        else:
            return render(request, 'book.html', {'form': booking_form})


class CancelView(View):
    """
    This view is the begin to the user cancel their
    booking. We collect their id and full name.
    If found we progress to CancelConfirmView
    """
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'book.cancel.html', {
                'form': FindBookingForm()
            }
        )

    def post(self, request, *args, **kwargs):

        cancel_form = FindBookingForm(data=request.POST)

        if cancel_form.is_valid():
            name = cancel_form.cleaned_data.get('your_name')
            booking_id = cancel_form.cleaned_data.get('your_booking_id')

            find_booking = get_booking(self, booking_id, name)

            if find_booking is not False:
                return redirect('cancel-confirm', id=find_booking.id)

            else:
                messages.warning(request, "We couldn't find your booking ")
                return render(
                    request,
                    'book.cancel.html', {
                        'form': FindBookingForm
                    }
                )


def CancelConfirmView(request, id):
    """
    This view is to make sure that the user
    really wants to cancel their booking
    """
    queryset = Booking.objects.get(id=id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('cancel')

    return render(request, 'book.cancel.confirm.html')


class EditView(View):
    """
    This view is the initial to the user edit their
    booking. We collect their id and full name.
    If found we progress to EditDetailsView
    """
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'book.edit.html', {
                'form': FindBookingForm()
            }
        )

    def post(self, request, *args, **kwargs):

        edit_form = FindBookingForm(data=request.POST)

        if edit_form.is_valid():
            name = edit_form.cleaned_data.get('your_name')
            booking_id = edit_form.cleaned_data.get('your_booking_id')

            find_booking = get_booking(self, booking_id, name)

            if find_booking is not False:
                return redirect('edit-details', id=find_booking.id)

            else:
                messages.warning(request, "We couldn't find your booking ")
                return render(
                    request,
                    'book.edit.html', {
                        'form': FindBookingForm
                    }
                )


def EditDetailsView(request, id):
    """
    This view is for the user edit their bookings,
    they can edit everything in ther booking
    """
    # Queryset the existing booking
    queryset = Booking.objects.get(id=id)
    # Pre populate the form fields, with the
    # queryset values
    data_dict = {'full_name': queryset.full_name,
                 'party_size': queryset.party_size,
                 'booking_date_start': queryset.booking_date_start,
                 'email': queryset.email,
                 'phone_number': queryset.phone_number}

    if request.method == 'POST':
        minutes_slot = 90
        delta = timedelta(minutes=minutes_slot)
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)

            # Getting input date to check if is there's table available
            required_size = booking.party_size
            required_start_time = booking.booking_date_start
            numbers_booked = avoid_double_booking(required_start_time)

            # If the booking date changes, we assign a new table,
            # if not we keep the same table
            if queryset.booking_date_start != booking.booking_date_start:
                table = get_right_table_available(required_start_time,
                                                  required_size)
            else:
                table = queryset.table

            # Explaining for user that there's no table
            # available at the required time
            if table == "No Table available":
                messages.warning(request, 'Sorry, there is no table'
                                          ' available at this time,'
                                          ' please try another date')
                return render(request, 'book.html', {'form': booking_form})

            # Explaining for user that they cant double book
            if booking.phone_number in numbers_booked:
                messages.warning(request, 'You already has'
                                          ' a booking at this time')
                return render(request, 'book.html', {'form': booking_form})

            # Passing booking end date to the Booking Model
            booking.booking_date_end = required_start_time + delta
            # Passing the table found to the Booking Model
            booking.table = table
            # Updating the booking
            queryset.full_name = booking.full_name
            queryset.party_size = booking.party_size
            queryset.booking_date_start = booking.booking_date_start
            queryset.booking_date_end = booking.booking_date_end
            queryset.email = booking.email
            queryset.table = booking.table
            queryset.phone_number = booking.phone_number
            queryset.save()

            # Send an email to user save their booking details
            message = email_message(queryset.full_name,
                                    queryset.booking_date_start,
                                    queryset.id)
            send_mail("Booking Confirmation",
                      message, settings.EMAIL_HOST_USER, [queryset.email],
                      fail_silently=False)
            return render(request, 'book.success.html', {
                          'name': queryset.full_name,
                          'group': queryset.party_size,
                          'date': queryset.booking_date_start,
                          'contact_number': queryset.phone_number,
                          'email': queryset.email,
                          'id': queryset.id}
                          )
        else:
            return render(request, 'book.html', {'form': booking_form})

    return render(
                    request,
                    'book.edit.details.html', {
                        'form': BookingForm(initial=data_dict)
                    }
                )


def get_right_table_available(required_start_time, required_size):
    """
    This method returns the smallest table available of the restaurant.
    Checks if the table has enough size for the party size.
    Checks if the is being used at the required booking time.
    Each booking has 90 minutes.
    """

    delta = timedelta(minutes=90)  # 90 min beacuse each bookins has 90min
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
        size__gte=required_size
        ).exclude(id__in=tables_booked_ids).order_by('size')

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
    delta = timedelta(minutes=90)  # 90 min beacuse each bookins has 90min
    required_end_time = required_start_time + delta

    start_date = required_start_time
    end_date = required_end_time

    all_numbers_booked = []

    # Get numbers which starts between the required booking time
    numbers_booked = Booking.objects.filter(
         booking_date_start__range=(start_date, end_date)
         ).values('phone_number')
    all_numbers_booked_temp = [x['phone_number'] for x in numbers_booked]
    all_numbers_booked = all_numbers_booked + all_numbers_booked_temp

    # Get numbers which ends between the required booking time
    numbers_booked = Booking.objects.filter(
         booking_date_end__range=(start_date, end_date)).values('phone_number')
    all_numbers_booked_temp = [x['phone_number'] for x in numbers_booked]
    all_numbers_booked = all_numbers_booked + all_numbers_booked_temp

    return all_numbers_booked


def get_booking(self, booking_id, name):
    """
    This funtion gets the booking wanted by the user
    if it exists, we carry on to Edit Booking,
    or to Cancel Booking.
    """
    try:
        return Booking.objects.get(
            full_name=name, id=booking_id)
    except Booking.DoesNotExist:
        return False


def email_message(name, date, id):
    """
    This function is only to create the message
    which will be sent by email to the user
    """
    message = f"""Hello {name}. We are looking forward to serving you.
These are your booking details:
Booking Date: {date},
Booking Reference ID: {id}

Best Wishes
Ask Japanese Team"""

    return message
