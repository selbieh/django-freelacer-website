# Generated by Django 2.0.4 on 2018-09-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_auto_20180912_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='specialty',
            field=models.CharField(default='other', max_length=80),
        ),
    ]
