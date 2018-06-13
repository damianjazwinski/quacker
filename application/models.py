from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image_link = models.CharField(max_length=100, blank=True, null=True, verbose_name="image_link")
	description = models.CharField(max_length=1000, blank=True, null=True, verbose_name="description")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Quack(models.Model):
    content = models.CharField(max_length=250)
    quacker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quacker')
    created_at = models.DateTimeField(auto_now=True)

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')

class OptionalMention(models.Model):
    quack = models.ForeignKey(Quack, on_delete=models.CASCADE, related_name='quack')
    mention = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mention')
