from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(null=False, max_length=255)
    last_name = models.CharField(null=False, max_length=255)
    email = models.CharField(null=False, max_length=64, unique=True)
    password = models.CharField(max_length = 255, null=False)
    birth_date = models.DateField(null=False)
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
        ('RNS','Rather Not Say')
    ]
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default='RNS')
    class Meta:
        ordering = ['first_name']
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']