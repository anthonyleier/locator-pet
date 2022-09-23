from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.CharField(max_length=165)
    slug = models.SlugField()
    status = models.CharField(max_length=15)
    publicado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imagem1 = models.ImageField(upload_to='localizador/upload/%Y/%m/%d/', null=True, blank=True)
    imagem2 = models.ImageField(upload_to='localizador/upload/%Y/%m/%d/', null=True, blank=True)
    imagem3 = models.ImageField(upload_to='localizador/upload/%Y/%m/%d/', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True),

    def __str__(self):
        return self.titulo
