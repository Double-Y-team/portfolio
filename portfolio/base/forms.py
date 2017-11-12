from django.contrib.auth.models import User
from django import forms
from .models import *


class UserCreateForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    email = models.EmailField()

    class Meta:
        model = User
        fields =['username', 'email',  'password']



class UserLoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =['username',  'password']