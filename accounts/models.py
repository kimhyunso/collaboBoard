from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Auth(models.Model):
    level = models.IntegerField()
    task = models.CharField(max_length=20)


class User(AbstractUser):
    auth = models.ForeignKey(Auth, related_name="user", on_delete=models.CASCADE)
    ID_user = models.CharField(max_length=20)
    PW_user = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)