from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: joao.silva'}),
        error_messages={'required': _('Username must not be empty.')},
        label=_('User')
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Your password')}),
        error_messages={'required': _('Password must not be empty.')},
        label=_('Password')
    )
