from django import forms
from django.utils.translation import gettext_lazy as _
from locator.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'neighborhood', 'city', 'image1', 'image2', 'image3']

    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Missing dog')}),
        error_messages={'required': _('Title must not be empty.')},
        label='Título'
    )

    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Description and facts')}),
        error_messages={'required': _('Description must not be empty.')},
        label='Descrição'
    )

    neighborhood = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Ex.: Center')}),
        error_messages={'required': _('Neighborhood must not be empty.')},
        label='Bairro'
    )

    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Caçador-SC'}),
        error_messages={'required': _('City must not be empty.')},
        label='Cidade'
    )

    image1 = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='Imagem 1'
    )

    image2 = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='Imagem 2'
    )

    image3 = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='Imagem 3'
    )
