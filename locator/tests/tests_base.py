from django.test import TestCase
from locator.models import Post
from django.contrib.auth.models import User


class LocatorTestBase(TestCase):
    def criarAutor(self):
        autor = User.objects.create_user(
            first_name="Anthony",
            last_name="Cruz",
            username="anthony.cruz",
            password="alfa@2020",
            email="anthony.cruz@alfatransportes.com.br")
        return autor

    def criarPost(self, publicado=True, titulo='Labrador desaparecido', slug='labrador-desaparecido-testes'):
        autor = User.objects.all().first()
        post = Post.objects.create(
            titulo=titulo,
            descricao='Labrador desaparecido ontem',
            slug=slug,
            status='Encontrado',
            publicado=publicado,
            imagem1='locator/upload/2022/09/23/chihuahua.jpg',
            autor=autor)
        return post

    def limparPosts(self):
        posts = Post.objects.all()
        for post in posts:
            post.delete()