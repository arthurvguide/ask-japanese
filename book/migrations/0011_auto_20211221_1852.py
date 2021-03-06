# Generated by Django 3.2 on 2021-12-21 18:52

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_alter_booking_booking_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date_end',
            field=models.DateTimeField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date_start',
            field=models.DateTimeField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
