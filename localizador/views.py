from django.shortcuts import render
from datetime import datetime
from random import randint

post_dados = {
    'id': randint(0, 100),
    'titulo': 'Labrador desaparecido',
    'descricao': 'O elemento sumiu na noite de ontem durante a queima de fogos.',
    'autor': 'Anthony Cruz',
    'created_at': datetime.now(),
    'updated_at': datetime.now(),
    'imagem': 'localizador/img/golden.jfif'
}


def homepage(request):
    dados = [post_dados, post_dados, post_dados, post_dados]
    return render(request, 'localizador/pages/homepage.html', context={'dados': dados})


def post(request, id):
    dado = post_dados
    return render(request, 'localizador/pages/post.html', context={'dado': dado})
