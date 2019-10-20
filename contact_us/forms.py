from .models import contact_us
from django.forms.models import ModelForm
from phonenumber_field.formfields import PhoneNumberField



class contact_us_form(ModelForm):
    phone=PhoneNumberField(required=False)
    class Meta:
        model=contact_us
        fields=['full_name','e_mail','phone','message']
