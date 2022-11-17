from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=65)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    found = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image1 = models.ImageField(upload_to='locator/upload/%Y/%m/%d/', null=True, blank=True)
    image2 = models.ImageField(upload_to='locator/upload/%Y/%m/%d/', null=True, blank=True)
    image3 = models.ImageField(upload_to='locator/upload/%Y/%m/%d/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detailPost', args=[self.id])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user} | {self.phone} | {self.address}"
