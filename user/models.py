from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=300, null = True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    USER_TYPE_CHOICES = [
        ('Student', 'Student'),
        ('Librarian', 'Librarian'),
        ('Teacher','Teacher'),
        ('Owner','Owner')
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

