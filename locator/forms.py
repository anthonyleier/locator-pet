from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.functions import addAttr, addPlaceholder, verifyStrongPassword


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    addAttr(username, 'class', 'form-control')
    addAttr(password, 'class', 'form-control')

    username.label = 'Usuário'
    password.label = 'Senha'


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        addPlaceholder(self.fields['first_name'], 'Ex.: John')
        addPlaceholder(self.fields['last_name'], 'Ex.: Smith')
        addPlaceholder(self.fields['username'], 'Ex.: jonh.smith')
        addPlaceholder(self.fields['email'], 'Ex.: jonh.smith@gmail.com')
        addPlaceholder(self.fields['password'], 'Sua senha')
        addPlaceholder(self.fields['password_confirm'], 'Sua senha novamente')

        addAttr(self.fields['first_name'], 'class', 'form-control')
        addAttr(self.fields['last_name'], 'class', 'form-control')
        addAttr(self.fields['username'], 'class', 'form-control')
        addAttr(self.fields['email'], 'class', 'form-control')
        addAttr(self.fields['password'], 'class', 'form-control')
        addAttr(self.fields['password_confirm'], 'class', 'form-control')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        error_messages={'required': 'Senha não pode ser vazia.'},
        help_text=('Necessário conter uma letra minúscula, uma letra maiúscula e um número. Tamanho mínimo de 8 caracteres.'),
        validators=[verifyStrongPassword],
        label='Senha'
    )

    password_confirm = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        error_messages={'required': 'Confirmação de senha não pode ser vazia.'},
        label='Confirmação de senha'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email)

        if exists:
            raise ValidationError('Este email já está em uso.', code='invalid')

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            error = ValidationError('As senhas devem ser iguais.', code='invalid')
            raise ValidationError({'password': error, 'password_confirm': error})
