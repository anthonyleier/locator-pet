from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from locator.models import Profile


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(author=instance)
        profile.save()
