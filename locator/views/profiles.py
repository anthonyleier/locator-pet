from locator.models import Profile
from django.shortcuts import render
from django.contrib.auth.models import User


def details(request, id):
    profile = Profile.objects.get(author_id=id)
    return render(request, 'locator/pages/profile.html', context={'profile': profile})
