from django import forms
from locator.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image1', 'image2', 'image3']

    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Labrador Desaparecido'}),
        error_messages={'required': 'Título não pode ser vazio.'},
        label='Título'
    )

    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição dos fatos e informações relevantes'}),
        error_messages={'required': 'Descrição não pode ser vazia.'},
        label='Descrição'
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
