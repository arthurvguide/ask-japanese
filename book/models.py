from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Table(models.Model):
    size = models.IntegerField(
        default=2)

    class Meta:
        ordering = ["-size"]
    
    def __str__(self):
        return str(self.size)


class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    party_size = models.IntegerField(
        default=2)
    booking_date_start = models.DateTimeField(
        default=0,
        blank=False,
        )
    
    booking_date_end = models.DateTimeField(
        default=0,
        blank=False,
        )
    phone_number = PhoneNumberField(null=False, blank=False)

    class Meta:
        ordering = ["booking_date_start"]

    def __str__(self):
        return self.full_name
