# Generated by Django 2.0.4 on 2018-07-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advertis', '0002_auto_20180430_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField(max_length=100)),
                ('data', models.CharField(max_length=200)),
            ],
        ),
    ]
