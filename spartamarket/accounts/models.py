from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=10, unique=True)# unique=True 닉네임 중복불가
    birthday = models.DateField()
    email = models.EmailField() 