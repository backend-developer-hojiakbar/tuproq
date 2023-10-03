from django import forms
from .models import Royxat


class royxatForm(forms.ModelForm):
    class Meta:
        model = Royxat
        fields ='__all__'