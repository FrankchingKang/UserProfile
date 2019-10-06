from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField()
    date_of_birth = models.DateField()
    bio = models.TextField()
    avatar = models.ImageField()
