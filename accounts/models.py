from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from .spc_choises import JOb_CHOICES,GRENDER
from multiselectfield import MultiSelectField



class userprofile(models.Model):



    user=models.OneToOneField('auth.User',related_name='profile',on_delete=models.CASCADE)
    pic=models.ImageField(upload_to="profile/profile_pic",blank=True)
    phone=PhoneNumberField(blank=True)
    whatsapp=PhoneNumberField(blank=True)
    resume=models.FileField(upload_to="profile/resume",blank=True)
    other_contact=models.CharField(max_length=120,blank=True)
    country=CountryField()
    specialty=MultiSelectField(choices=JOb_CHOICES)
    Grender=models.CharField(max_length=7,choices=GRENDER,default="Male")
    private=models.BooleanField(default=False,verbose_name="Enable employer to see my private data like (phone,whatsapp,..etc)" )
    free_lancer=models.BooleanField(default=False,verbose_name="Include me in free lancer lists")
    def __str__(self):
        return self.user.username



def creat_profile(sender,**kwargs):
    if kwargs["created"]:
        user_profile=userprofile.objects.create(user=kwargs["instance"])
post_save.connect(creat_profile,sender=User)
