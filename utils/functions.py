import os
import re
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def verifyStrongPassword(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(('Sua senha é muito fraca.'), code='invalid')


def verifyExistingEmail(email):
    exists = User.objects.filter(email=email)
    if exists:
        raise ValidationError('Este email já está em uso.', code='invalid')


def resizeImage(image, newWidth=800, quality=50):
    if image:
        path = os.path.join(settings.MEDIA_ROOT, image.name)
        image = Image.open(path)
        width, height = image.size

        if width > newWidth:
            height = (height * newWidth) / width
            width = newWidth

        newImage = image.resize((width, height), Image.LANCZOS)
        newImage.save(path, optimize=True, quality=50)

        image.close()
        newImage.close()
