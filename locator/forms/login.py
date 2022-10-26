from django import forms
from utils.functions import addAttr


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    addAttr(username, 'class', 'form-control')
    addAttr(password, 'class', 'form-control')

    username.label = 'Usuário'
    password.label = 'Senha'
