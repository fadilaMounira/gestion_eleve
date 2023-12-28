from django.core import validators
from django import forms
from .models import User

class enregistrementEleve(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']