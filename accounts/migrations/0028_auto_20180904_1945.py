# Generated by Django 2.0.4 on 2018-09-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20180904_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(upload_to='profile/profile_pic'),
        ),
    ]
