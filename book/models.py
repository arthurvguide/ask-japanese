from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator


class Table(models.Model):
    size = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(8),
            MinValueValidator(1)
        ]
     )

    class Meta:
        ordering = ["-size"]

    def __str__(self):
        return str(self.size)

class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    party_size = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(8),
            MinValueValidator(1)
        ]
     )
    booking_date_time_start = models.DateTimeField()
    booking_date_time_end = models.DateTimeField()
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)
    email = models.EmailField()
    
    class Meta:
        ordering = ["booking_date_time_start"]

    def __str__(self):
        return self.full_name
