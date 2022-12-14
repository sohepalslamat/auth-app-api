from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email= models.EmailField('email address', unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','username']

    def __str__(self):
        return self.username
