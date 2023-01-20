from django import forms 
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()
class modelsForm(forms.ModelForm):
    title = forms.CharField(min_length=2, max_length=100)
    

    class Meta:
        model = User
        fields = ('ID_user', 'ID_user',)