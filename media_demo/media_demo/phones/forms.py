from media_demo.phones.models import Phone
from django import forms


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'