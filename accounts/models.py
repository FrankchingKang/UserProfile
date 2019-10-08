from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=255, default='first name')
    last_name = models.CharField(max_length=255, default='last name')
    email = models.EmailField(default='example@example.com')
    date_of_birth = models.DateField(default='none')
    bio = models.TextField(default='bio')
    avatar = models.ImageField(upload_to='assets/images/')
