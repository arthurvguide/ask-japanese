# Generated by Django 3.2 on 2021-12-20 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20211220_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_end_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_start_time',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date_end',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
