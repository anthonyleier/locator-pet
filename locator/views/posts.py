import os

from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from locator.models import Post
from locator.forms.post import PostForm
from utils.functions import resizeImage

QTY_PER_PAGE = int(os.environ.get('QTY_PER_PAGE', 4))


def detailPost(request, id):
    post = get_object_or_404(Post, pk=id, published=True)
    return render(request, 'locator/pages/post.html', context={'post': post})


@login_required(login_url='loginForm')
def createPost(request):
    post = Post()
    form = PostForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.published = False
        post.slug = slugify(post.title)
        post.save()

        resizeImage(post.image1)
        resizeImage(post.image2)
        resizeImage(post.image3)

        messages.success(request, 'Seu post foi salvo com sucesso')
        return redirect('dashboard')
    return render(request, 'locator/pages/edit.html', context={'form': form, 'action': 'create', 'id': 0})


@login_required(login_url='loginForm')
def updatePost(request, id):
    post = Post.objects.get(pk=id, published=False, user=request.user)
    form = PostForm(request.POST or None, instance=post, files=request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.published = False
        post.save()

        resizeImage(post.image1)
        resizeImage(post.image2)
        resizeImage(post.image3)

        messages.success(request, 'Seu post foi salvo com sucesso')
        return redirect('dashboard')
    return render(request, 'locator/pages/edit.html', context={'form': form, 'action': 'update', 'id': id})


@login_required(login_url='loginForm')
def foundPost(request, id):
    post = Post.objects.get(pk=id, user=request.user)
    post.found = True
    post.save()
    messages.success(request, 'Que notícia maravilhosa!')
    return redirect('dashboard')


@login_required(login_url='loginForm')
def deletePost(request, id):
    post = Post.objects.get(pk=id, published=False, user=request.user)
    post.delete()
    messages.success(request, "Post deletado com sucesso!")
    return redirect('dashboard')
