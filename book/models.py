from datetime import datetime, date
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator


TIME_CHOICES = (
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'), 
)


class Table(models.Model):
    size = models.IntegerField(
        default=2,
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
    booking_date = models.DateField(
        default=datetime.now,
        blank=False,
        validators=[
            MinValueValidator(date.today())
        ])

    booking_time = models.CharField(default=TIME_CHOICES[21],
                   max_length=30, choices=TIME_CHOICES)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)

    class Meta:
        ordering = ["booking_date"]

    def __str__(self):
        return self.full_name
