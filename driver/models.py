# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    

class Banner(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='banners/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title or f"Banner {self.id}"


class DriverFeedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='driver_feedbacks',null=True,blank=True)
    image = models.ImageField(upload_to='driver_feedback/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Driver Feedback {self.id} - {self.user.username if self.user else 'No User'}"