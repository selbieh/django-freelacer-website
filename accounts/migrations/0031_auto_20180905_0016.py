# Generated by Django 2.0.4 on 2018-09-04 22:16

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20180904_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(upload_to="profile/profile_pic"),
        ),
    ]
