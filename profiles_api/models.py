import email
from statistics import mode
from unicodedata import name
from django.db import models

from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # objects =UserProfileManager()
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve Full Name of User"""
        return self.name

    def __str__(self) :
        """Return String Representation of Our User"""
        return self.email




