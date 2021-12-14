from django.contrib import admin
from .models import Table, Booking

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):

    search_fields = ['size']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'party_size', 'booking_date_time_start','booking_date_time_end')
    search_fields = ['full_name', 'booking_date_time_start']
