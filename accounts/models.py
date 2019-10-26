from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='first name')
    last_name = models.CharField(max_length=255, default='last name')
    email = models.EmailField(default='example@example.com')
    second_email = models.EmailField(default='Second_example@example.com')
    date_of_birth = models.DateField(null=True, blank=True,default='1900-01-01')
    bio = models.TextField(default='bio')
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
