import os
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from locator.models import Post
from utils.pagination import montarRangePaginacao, construirPaginacao


QUANTIDADE_POR_PAGINA = int(os.environ.get('QUANTIDADE_POR_PAGINA', 4))


def homepage(request):
    posts = Post.objects.filter(publicado=True).order_by('-id')
    pagina, pagination_range = construirPaginacao(request, posts, QUANTIDADE_POR_PAGINA)
    return render(request, 'locator/pages/homepage.html', context={'pagina': pagina, 'pagination_range': pagination_range.get('paginacao'), 'paginacao': pagination_range})


def post(request, id):
    post = get_object_or_404(Post, pk=id, publicado=True)
    return render(request, 'locator/pages/post.html', context={'post': post})


def search(request):
    busca = request.GET.get('q', '').strip()

    if not busca:
        raise Http404()

    posts = Post.objects.filter(Q(Q(titulo__icontains=busca) | Q(descricao__icontains=busca)), publicado=True)
    posts = posts.order_by('-id')

    pagina, pagination_range = construirPaginacao(request, posts, QUANTIDADE_POR_PAGINA)
    return render(request, 'locator/pages/search.html', context={'busca': busca, 'pagina': pagina, 'pagination_range': pagination_range.get('paginacao'), 'paginacao': pagination_range, 'parametroAdicional': f"&q={busca}"})
