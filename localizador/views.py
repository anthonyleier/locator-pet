from django.http import Http404
from django.shortcuts import render, get_object_or_404
from localizador.models import Post


def homepage(request):
    posts = Post.objects.filter(publicado=True).order_by('-id')
    return render(request, 'localizador/pages/homepage.html', context={'posts': posts})


def post(request, id):
    post = get_object_or_404(Post, pk=id, publicado=True)
    return render(request, 'localizador/pages/post.html', context={'post': post})


def search(request):
    busca = request.GET.get('q').strip()

    if not busca:
        raise Http404()

    return render(request, 'localizador/pages/search.html', context={'busca': busca})
