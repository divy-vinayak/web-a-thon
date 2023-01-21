from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    roll_no = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    college = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'


