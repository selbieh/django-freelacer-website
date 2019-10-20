# Generated by Django 2.0.4 on 2018-04-30 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Advertis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='adver_m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('details', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('field', models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='adver',
            name='user',
        ),
        migrations.DeleteModel(
            name='adver',
        ),
    ]
