from datetime import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator


TIME_CHOICES = (
    (0, '11:00'),
    (1, '11:30'),
    (2, '12:00'),
    (3, '12:30'),
    (4, '13:00'),
    (5, '13:30'),
    (6, '14:00'),
    (7, '14:30'),
    (8, '15:00'),
    (9, '15:30'),
    (10, '16:00'),
    (11, '16:30'),
    (12, '17:00'),
    (13, '17:30'),
    (14, '18:00'),
    (15, '18:30'),
    (16, '19:00'),
    (17, '19:30'),
    (18, '20:00'),
    (19, '20:30'),
    (20, '21:00'),
    (21, '21:30'), 
)


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
    booking_date = models.DateField(default=datetime.now, blank=False)
    booking_time = models.CharField(default=TIME_CHOICES[21],
        max_length=30, choices=TIME_CHOICES)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    
    class Meta:
        ordering = ["booking_date"]

    def __str__(self):
        return self.full_name
