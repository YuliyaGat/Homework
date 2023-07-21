from django import forms
from .models import Web_sites


class MediaForm(forms.ModelForm):
    class Meta:
        model = Web_sites
        fields = '__all__'