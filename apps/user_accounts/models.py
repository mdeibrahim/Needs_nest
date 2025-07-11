from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from .manager import UserManager


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    username = None

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    
    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)