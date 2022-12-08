import os
import re
from PIL import Image

from django.conf import settings
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from locator.models import Post


def verifyFileType(file):
    filePath = os.path.splitext(file.name)
    fileExtension = filePath[1].lower()
    validExtensions = ['.jpg', '.jpeg', '.png']

    if fileExtension not in validExtensions:
        raise ValidationError(_('Unsupported file extension'), code='invalid')


def verifyStrongPassword(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(_('Your password is too weak'), code='invalid')


def verifyExistingEmail(email):
    exists = User.objects.filter(email=email)
    if exists:
        raise ValidationError(_('This email are already in use'), code='invalid')


def resizeImage(image, newWidth=800, quality=50):
    if image:
        path = os.path.join(settings.MEDIA_ROOT, image.name)
        image = Image.open(path)
        width, height = image.size

        if width > newWidth:
            height = (height * newWidth) / width
            width = newWidth

        width = round(width)
        height = round(height)

        newImage = image.resize((width, height), Image.LANCZOS)
        newImage.save(path, optimize=True, quality=quality)

        image.close()
        newImage.close()


def makeSlug(text):
    slug = slugify(text)
    exists = Post.objects.filter(slug=slug)

    if exists:
        slug += "-new"
        return makeSlug(slug)

    return slug
