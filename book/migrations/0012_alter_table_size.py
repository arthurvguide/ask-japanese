# Generated by Django 3.2 on 2021-12-21 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20211221_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='size',
            field=models.IntegerField(default=2),
        ),
    ]