from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):

    name = models.CharField("Nombre", max_length=30, blank=True)

    email = models.EmailField("email", unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
      
    objects = UserManager()
    def __str__(self):
        return self.email

    


