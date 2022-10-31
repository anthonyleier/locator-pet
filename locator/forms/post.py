from django import forms
from locator.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'status', 'image1', 'image2', 'image3']
