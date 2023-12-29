from django.core import validators
from django import forms
from .models import User

class enregistrementEleve(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password','niveau','naissance','sexe']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'naissance': forms.TextInput(attrs={'class':'form-control'}),
            'sexe' : forms.TextInput(attrs={'class':'form-control'}),
            'niveau': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }