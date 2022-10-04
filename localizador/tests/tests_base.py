from django.test import TestCase
from localizador.models import Post
from django.contrib.auth.models import User


class LocalizadorTestBase(TestCase):
    def criarAutor(self):
        autor = User.objects.create_user(
            first_name="Anthony",
            last_name="Cruz",
            username="anthony.cruz",
            password="alfa@2020",
            email="anthony.cruz@alfatransportes.com.br")
        return autor

    def criarPost(self, publicado=True):
        autor = self.criarAutor()
        post = Post.objects.create(
            titulo='Labrador desaparecido',
            descricao='Labrador desaparecido ontem',
            slug='labrador-desaparecido',
            status='Encontrado',
            publicado=publicado,
            imagem1='localizador/upload/2022/09/23/chihuahua.jpg',
            autor=autor)
        return post

    def limparPosts(self):
        posts = Post.objects.all()
        for post in posts:
            post.delete()
