from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.functions import verifyExistingEmail, verifyStrongPassword


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: João'}),
        error_messages={'required': 'Primeiro nome não pode ser vazio.'},
        label='Primeiro nome'
    )

    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Silva'}),
        error_messages={'required': 'Último nome não pode ser vazio.'},
        label='Último nome'
    )

    username = forms.CharField(
        required=True,
        min_length=4,
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: joao.silva'}),
        error_messages={
            'required': 'Usuário não pode ser vazio.',
            'min_length': 'Usuário deve ter no mínimo 4 caracteres',
            'max_length': 'Usuário deve ter no máximo 150 caracteres'
        },
        help_text=('Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.'),
        label='Usuário'
    )

    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: joao.silva@gmail.com'}),
        error_messages={'required': 'Email não pode ser vazio.'},
        validators=[verifyExistingEmail],
        label='Email'
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Sua senha'}),
        error_messages={'required': 'Senha não pode ser vazia.'},
        help_text=('Necessário conter uma letra minúscula, uma letra maiúscula e um número. Tamanho mínimo de 8 caracteres.'),
        validators=[verifyStrongPassword],
        label='Senha'
    )

    password_confirm = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Sua senha novamente'}),
        error_messages={'required': 'Confirmação de senha não pode ser vazia.'},
        label='Confirmação de senha'
    )

    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: (49) 9 99876543'}),
        error_messages={'required': 'Telefone não pode ser vazio.'},
        help_text=('Será utilizado para os outros usuários entrarem em contato.'),
        label='Telefone'
    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            error = ValidationError('As senhas devem ser iguais.', code='invalid')
            raise ValidationError({'password': error, 'password_confirm': error})
