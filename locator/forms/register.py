from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from utils.functions import verifyExistingEmail, verifyStrongPassword


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Ex.: John')}),
        error_messages={'required': _('First name must not be empty.')},
        label=_('First Name')
    )

    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Ex.: Smith')}),
        error_messages={'required': _('Last name must not be empty.')},
        label=_('Last Name')
    )

    username = forms.CharField(
        required=True,
        min_length=4,
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Ex.: john.smith')}),
        error_messages={
            'required': _('Username must not be empty.'),
            'min_length': _('Username must be at least 4 characters long.'),
            'max_length': _('Username must be a maximum of 150 characters.'),
        },
        help_text=('Obligatoriness. 150 characters or less. Only letters, numbers and @/./+/-/_.'),
        label=_('Username')
    )

    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Ex.: john.smith@gmail.com')}),
        error_messages={'required': _('Email must not be empty.')},
        validators=[verifyExistingEmail],
        label=_('Email')
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Your password')}),
        error_messages={'required': _('Password must not be empty.')},
        help_text=(_('The password must have at least one uppercase letter, one lowercase letter and one number. Minimum length of 8 characters.')),
        validators=[verifyStrongPassword],
        label=_('Password')
    )

    password_confirm = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Your password again')}),
        error_messages={'required': _('Password confirm must not be empty.')},
        label=_('Password confirm')
    )

    phone = forms.CharField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: 49999876543'}),
        error_messages={'required': _('Phone must not be empty.')},
        help_text=(_('Phone will be used for other users to contact you.')),
        label=_('Phone')
    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            error = ValidationError(_('Passwords must be the same.'), code='invalid')
            raise ValidationError({'password': error, 'password_confirm': error})
