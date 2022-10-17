from django import forms
from django.contrib.auth.models import User


def addAttr(field, attrName, attrValue):
    existingAttr = field.widget.attrs.get(attrName)
    newAttr = f"{existingAttr} {attrValue}".strip() if existingAttr else attrValue
    field.widget.attrs[attrName] = newAttr


def addPlaceholder(field, attrValue):
    field.widget.attrs['placeholder'] = attrValue


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

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your password here'
        }),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter, one lowercase letter and one number.',
            'The length should be at least 8 characters.'
        )
    )

    password_confirm = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repeat your password here'
        })
    )
