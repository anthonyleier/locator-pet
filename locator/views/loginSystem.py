from django.http import Http404
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _

from locator.forms.login import LoginForm
from locator.forms.register import RegisterForm


def registerForm(request):
    form_data = request.session.get('form_data')
    form = RegisterForm(form_data)
    context = {'form': form, 'type': 'Register', 'route': 'registerAction'}
    return render(request, 'locator/pages/auth.html', context=context)


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
        messages.success(request, _('Seu usuário foi criado com sucesso, faça o login'))
        del (request.session['form_data'])
        return redirect('loginForm')

    return redirect('registerForm')


def loginForm(request):
    authenticatedUser = request.user.is_authenticated
    if authenticatedUser:
        return redirect('dashboard')

    form = LoginForm()
    context = {'form': form, 'type': 'Login', 'route': 'loginAction'}
    return render(request, 'locator/pages/auth.html', context=context)


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
