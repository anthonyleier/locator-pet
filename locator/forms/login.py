from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: joao.silva'}),
        error_messages={'required': 'Login não pode ser vazio.'},
        label='Usuário'
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Sua senha'}),
        error_messages={'required': 'Senha não pode ser vazia.'},
        label='Senha'
    )
