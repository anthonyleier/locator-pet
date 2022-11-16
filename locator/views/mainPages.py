import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from locator.models import Post
from utils.pagination import makePagination


QTY_PER_PAGE = int(os.environ.get('QTY_PER_PAGE', 4))


def home(request):
    posts = Post.objects.filter(published=True).order_by('-id')
    page, paginationInfo = makePagination(request, posts, QTY_PER_PAGE)
    return render(request, 'locator/pages/home.html', context={
        'page': page,
        'tinyRange': paginationInfo.get('tinyRange'),
        'paginationInfo': paginationInfo
    })


@login_required(login_url='loginForm')
def dashboard(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'locator/pages/dashboard.html', context={'posts': posts})
