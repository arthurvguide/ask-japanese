from django.contrib import admin
from .models import Table, Booking

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):

    search_fields = ['size']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'party_size', 'booking_date_start')
    search_fields = ['full_name']
    list_filter = ['booking_date_start']