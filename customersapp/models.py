from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=1)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return (self.first_name+' '+self.last_name)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


def post_user_create(sender, instance, created, **kwargs):
    #print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_create, sender=User)