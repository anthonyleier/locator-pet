from django.shortcuts import render


def homepage(request):
    return render(request, 'localizador/pages/homepage.html')
