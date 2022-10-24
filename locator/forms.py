import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def addAttr(field, attrName, attrValue):
    existingAttr = field.widget.attrs.get(attrName)
    newAttr = f"{existingAttr} {attrValue}".strip() if existingAttr else attrValue
    field.widget.attrs[attrName] = newAttr


def addPlaceholder(field, attrValue):
    field.widget.attrs['placeholder'] = attrValue


def verifyStrongPassword(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(('Fracokk'), code='invalid')


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
        addPlaceholder(self.fields['password'], 'Your password')
        addPlaceholder(self.fields['password_confirm'], 'Your password again')

        addAttr(self.fields['first_name'], 'class', 'form-control')
        addAttr(self.fields['last_name'], 'class', 'form-control')
        addAttr(self.fields['username'], 'class', 'form-control')
        addAttr(self.fields['email'], 'class', 'form-control')
        addAttr(self.fields['password'], 'class', 'form-control')
        addAttr(self.fields['password_confirm'], 'class', 'form-control')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        error_messages={'required': 'Password must not be empty'},
        help_text=('Password must have at least one uppercase letter, one lowercase letter and one number. The length should be at least 8 characters.'),
        validators=[verifyStrongPassword],
        label='Password'
    )

    password_confirm = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        label='Password confirm'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        exists = User.objects.filter(email=email)

        if exists:
            error = ValidationError('Email tem que ser diferente')
            raise ValidationError({'email': error})

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            error = ValidationError('Password and password validation must be the same', code='invalid')
            raise ValidationError({'password': error, 'password_confirm': error})


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )