from django.forms.models import ModelForm
from .models import adver_m


class advir_form(ModelForm):
    class Meta:
     model=adver_m
     fields=['title','details','field']


