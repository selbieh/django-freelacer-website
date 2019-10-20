# Generated by Django 2.0.4 on 2018-05-02 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20180502_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(blank=True, upload_to='media/profile/profile_pic'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='resume',
            field=models.FileField(blank=True, max_length=1800, upload_to='media/profile/cv'),
        ),
    ]
