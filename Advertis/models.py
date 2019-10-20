from django.db import models
from django.contrib.auth.models import User
from .adv_choises import JOb_CHOICES,status_choises


class adver_m (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=120,blank=False)
    details=models.TextField(max_length=500,blank=False)
    date=models.DateField(auto_now_add=True)
    field=models.CharField(max_length=50,choices=JOb_CHOICES,default='Other')
    status=models.CharField(max_length=22,choices=status_choises,default="waiting admin approval")

    def __str__(self):
        return self.title


