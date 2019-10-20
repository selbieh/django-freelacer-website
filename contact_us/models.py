from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class contact_us(models.Model):
    full_name=models.CharField(max_length=120,blank=False)
    e_mail=models.EmailField(blank=False)
    message=models.TextField(blank=False)
    phone=PhoneNumberField(blank=True)
    def __str__(self):
        return self.full_name







# Create your models here.
