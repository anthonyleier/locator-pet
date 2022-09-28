from django.shortcuts import render
from localizador.models import Post


def homepage(request):
    posts = Post.objects.filter(publicado=True).order_by('-id')
    return render(request, 'localizador/pages/homepage.html', context={'posts': posts})


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'localizador/pages/post.html', context={'post': post})
