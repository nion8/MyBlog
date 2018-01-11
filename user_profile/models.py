from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    usermname = models.CharField('username', max_length=23, unique=True, db_index=True)
    email = models.EmailField('email adress', unique=True)
    




