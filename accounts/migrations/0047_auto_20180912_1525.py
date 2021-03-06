# Generated by Django 2.0.4 on 2018-09-12 13:25

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_auto_20180912_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Grender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=7),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='whatsapp',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
    ]
