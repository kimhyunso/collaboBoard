from django import forms 
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()
class UserForm(UserCreationForm):
    title = forms.CharField(min_length=2, max_length=100)
    class Meta:
        model = User
        fields = ('ID_user', 'PW_user')