from django.forms.models import ModelForm
from .models import userprofile
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .spc_choises import JOb_CHOICES
from django import forms




class profile_form(ModelForm):
    specialty=forms.MultipleChoiceField(choices=JOb_CHOICES)

    class Meta:
        model=userprofile
        fields=['phone','whatsapp','other_contact',"Grender",'country','pic','resume',"private","specialty","free_lancer"]


class CustomForm(RegistrationFormUniqueEmail):

    first_name = forms.CharField(required=True)
    last_name =forms.CharField(required=True)
    class Meta:
        model=User
        fields=['first_name','last_name',"username",'email','password1','password2']
        def save(self,commit=True):
            user=super(CustomForm,self).save(commit=False)
            user.first_name=self.cleaned_data['first_name']
            user.last_name=self.cleaned_data['last_name']
            if commit:
                user.save()
                return user

class personal_f(UserChangeForm):
    class Meta:
        model=User
        fields=["username",'email','first_name','last_name',"password"]



