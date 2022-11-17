import os
from django.http import Http404
from django.shortcuts import render
from django.db.models import Q
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


def search(request):
    searchTerm = request.GET.get('q', '').strip()

    if not searchTerm:
        raise Http404()

    posts = Post.objects.filter(Q(Q(title__icontains=searchTerm) | Q(description__icontains=searchTerm)), published=True)
    posts = posts.order_by('-id')
    page, paginationInfo = makePagination(request, posts, QTY_PER_PAGE)

    return render(request, 'locator/pages/home.html', context={
        'searchTerm': searchTerm,
        'page': page,
        'tinyRange': paginationInfo.get('tinyRange'),
        'paginationInfo': paginationInfo,
        'additionalParam': f"&q={searchTerm}"
    })


@login_required(login_url='loginForm')
def dashboard(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'locator/pages/dashboard.html', context={'posts': posts})
