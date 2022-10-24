import os
from django.db.models import Q
from locator.models import Post
from django.http import Http404
from locator.forms import RegisterForm, LoginForm
from utils.pagination import makePagination
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


QTY_PER_PAGE = int(os.environ.get('QTY_PER_PAGE', 4))


def home(request):
    posts = Post.objects.filter(published=True).order_by('-id')
    page, paginationInfo = makePagination(request, posts, QTY_PER_PAGE)
    return render(request, 'locator/pages/home.html', context={
        'page': page,
        'tinyRange': paginationInfo.get('tinyRange'),
        'paginationInfo': paginationInfo
    })


def post(request, id):
    post = get_object_or_404(Post, pk=id, published=True)
    return render(request, 'locator/pages/post.html', context={'post': post})


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


def registerForm(request):
    form_data = request.session.get('form_data')
    form = RegisterForm(form_data)
    return render(request, 'locator/pages/register.html', context={'form': form})


def registerCreate(request):
    if not request.POST:
        raise Http404()

    form_data = request.POST
    request.session['form_data'] = form_data

    form = RegisterForm(form_data)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Your user is created, please log in.')
        del (request.session['form_data'])

    return redirect('locator:loginForm')


def loginForm(request):
    form = LoginForm()
    return render(request, 'locator/pages/login.html', context={'form': form})


def loginAccess(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    if form.is_valid():
        authenticatedUser = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', '')
        )

        if authenticatedUser:
            login(request, authenticatedUser)
            messages.success(request, 'Usuário logado com sucesso')
        else:
            messages.error(request, 'Usuário inválido')

    else:
        messages.error(request, 'Erro na validação')

    return redirect('locator:loginForm')


@login_required(login_url='locator:loginForm')
def logoutAccess(request):
    if not request.POST:
        return redirect('locator:loginForm')

    if request.POST.get('username') != request.user.username:
        return redirect('locator:loginForm')

    logout(request)
    return redirect('locator:loginForm')
