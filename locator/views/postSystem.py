import os
from django.db.models import Q
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from locator.models import Post
from utils.pagination import makePagination
from locator.forms.post import PostForm


QTY_PER_PAGE = int(os.environ.get('QTY_PER_PAGE', 4))


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


def post(request, id):
    post = get_object_or_404(Post, pk=id, published=True)
    return render(request, 'locator/pages/post.html', context={'post': post})


@login_required(login_url='loginForm')
def createPost(request):
    post = Post()
    form = PostForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published = False
        post.slug = slugify(post.title)
        post.save()
        messages.success(request, 'Seu post foi salvo com sucesso')
        return redirect('dashboard')
        # rezise image here

    return render(request, 'locator/pages/edit.html', context={'form': form, 'action': 'create', 'id': 0})


@login_required(login_url='loginForm')
def updatePost(request, id):
    post = Post.objects.get(pk=id, published=False, author=request.user)
    form = PostForm(request.POST or None, instance=post, files=request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published = False
        post.save()
        messages.success(request, 'Seu post foi salvo com sucesso')
        return redirect('dashboard')
        # rezise image here
    return render(request, 'locator/pages/edit.html', context={'form': form, 'action': 'update', 'id': id})


@login_required(login_url='loginForm')
def foundPost(request, id):
    post = Post.objects.get(pk=id, author=request.user)
    post.found = True
    post.save()
    messages.success(request, 'Que notícia maravilhosa!')
    return redirect('dashboard')


@login_required(login_url='loginForm')
def deletePost(request, id):
    post = Post.objects.get(pk=id, published=False, author=request.user)
    post.delete()

    # delete images here
    messages.success(request, "Post deletado com sucesso!")
    return redirect('dashboard')
