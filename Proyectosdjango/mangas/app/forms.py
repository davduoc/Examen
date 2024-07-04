from django import forms
from .models import Manga

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['nombre', 'tomo', 'editorial', 'precio']



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


