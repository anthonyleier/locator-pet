import os

from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete

from locator.models import Profile, Post


def deleteImages(instance):
    try:
        os.remove(instance.image1.path)
        os.remove(instance.image2.path)
        os.remove(instance.image3.path)

    except (ValueError, FileNotFoundError) as error:
        print(f"Arquivo para remoção não encontrado - {error}")


@receiver(post_save, sender=User)
def createProfile(instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()


@receiver(pre_delete, sender=Post)
def deleteImagesOnDeletePost(instance, *args, **kwargs):
    deleteImages(instance)
