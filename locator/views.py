import os
from django.db.models import Q
from django.http import Http404
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404

from locator.models import Post
from utils.pagination import makePagination

from locator.forms.login import LoginForm
from locator.forms.register import RegisterForm
from locator.forms.post import PostForm


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


def registerAction(request):
    if not request.POST:
        raise Http404()

    form_data = request.POST
    request.session['form_data'] = form_data
    form = RegisterForm(form_data)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Seu usuário foi criado com sucesso, faça o login')
        del (request.session['form_data'])
        return redirect('loginForm')

    return redirect('registerForm')


def loginForm(request):
    authenticatedUser = request.user.is_authenticated
    if authenticatedUser:
        return redirect('dashboard')

    form = LoginForm()
    return render(request, 'locator/pages/login.html', context={'form': form})


def loginAction(request):
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
            return redirect('dashboard')

        else:
            messages.error(request, 'Usuário inválido')

    else:
        messages.error(request, 'Erro na validação')

    return redirect('loginForm')


@login_required(login_url='loginForm')
def logoutAction(request):
    if not request.POST:
        return redirect('loginForm')

    if request.POST.get('username') != request.user.username:
        return redirect('loginForm')

    logout(request)
    return redirect('loginForm')


@login_required(login_url='loginForm')
def dashboard(request):
    publishedPosts = Post.objects.filter(published=True, author=request.user)
    notPublishedPosts = Post.objects.filter(published=False, author=request.user)
    return render(request, 'locator/pages/dashboard.html', context={'publishedPosts': publishedPosts, 'notPublishedPosts': notPublishedPosts})


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
    return render(request, 'locator/pages/create.html', context={'form': form})


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
        return redirect('updatePost', id)
    return render(request, 'locator/pages/update.html', context={'form': form, 'id': id})


@login_required(login_url='loginForm')
def deletePost(request, id):
    post = Post.objects.get(pk=id, published=False, author=request.user)
    post.delete()
    messages.success(request, "Post deletado com sucesso!")
    return redirect('dashboard')
