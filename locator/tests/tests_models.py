from locator.models import Post
from parameterized import parameterized
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from locator.tests.tests_base import LocatorTestBase


class LocatorModelsTest(LocatorTestBase):
    def setUp(self):
        self.post = self.criarPost()

    def test_post_titulo(self):
        self.post.titulo = '$' * 70

        with self.assertRaises(ValidationError):
            self.post.full_clean()  # Validação dos campos

    def test_post_campos_tamanho(self):
        campos = [
            ('titulo', 65),
            ('descricao', 165),
            ('status', 15)
        ]

        for campo, tamanho in campos:
            with self.subTest(campo=campo, tamanho=tamanho):
                setattr(self.post, campo, '$' * (tamanho + 1))
                with self.assertRaises(ValidationError):
                    self.post.full_clean()  # Validação dos campos

    @parameterized.expand([
        ('titulo', 65),
        ('descricao', 165),
        ('status', 15)
    ])
    def test_post_campos_tamanho_novo(self, campo, tamanho):
        setattr(self.post, campo, '$' * (tamanho + 1))
        with self.assertRaises(ValidationError):
            self.post.full_clean()  # Validação dos campos

    def test_post_publicado(self):
        autor = self.criarAutor()
        post = Post(
            titulo='Labrador desaparecido',
            descricao='Labrador desaparecido ontem',
            slug='labrador-desaparecido',
            status='Encontrado',
            imagem1='locator/upload/2022/09/23/chihuahua.jpg',
            autor=autor)
        post.full_clean()
        post.save()
        self.assertFalse(post.publicado)
