# Generated by Django 3.2.9 on 2021-12-13 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ['-size']},
        ),
    ]
