# Generated by Django 4.1 on 2022-11-05 04:34

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('socmapp', '0003_alter_appoinment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
