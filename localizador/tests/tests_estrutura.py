from django.test import TestCase
from localizador import views
from localizador.models import Post
from django.urls import reverse, resolve
from django.contrib.auth.models import User


class LocalizadorURLS(TestCase):
    def test_home_url(self):
        url = reverse('localizador:homepage')
        self.assertEqual(url, '/')

    def test_post_url(self):
        url = reverse('localizador:post', args=[2])
        self.assertEqual(url, '/posts/2')


class LocalizadorViewsTest(TestCase):
    def test_home_view(self):
        view = resolve(reverse('localizador:homepage'))
        self.assertIs(view.func, views.homepage)

    def test_post_view(self):
        view = resolve(reverse('localizador:post', args=[2]))
        self.assertIs(view.func, views.post)


class LocalizadorContentTest(TestCase):
    def test_home_status(self):
        response = self.client.get(reverse('localizador:homepage'))
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get(reverse('localizador:homepage'))
        self.assertTemplateUsed(response, 'localizador/pages/homepage.html')

    def test_home_vazio(self):
        response = self.client.get(reverse('localizador:homepage'))
        self.assertIn('Nenhum post cadastrado', response.content.decode('UTF8'))

    def test_post_404_status(self):
        response = self.client.get(reverse('localizador:post', args=[250]))
        self.assertEqual(response.status_code, 404)

    def test_home_com_posts(self):
        autor = User.objects.create_user(first_name="first", last_name="last", username="user", password="123456", email="user@gmail.com")
        Post.objects.create(titulo='Labrador desaparecido', descricao='Labrador desaparecido', slug='labrador-desaparecido', status='Encontrado', publicado=True, imagem1='localizador/upload/2022/09/23/chihuahua.jpg', imagem2='', imagem3='', autor=autor)
        response = self.client.get(reverse('localizador:homepage'))

        html = response.content.decode('UTF8')

        self.assertEqual(len(response.context['posts']), 1)
        self.assertEqual(response.context['posts'].first().titulo, "Labrador desaparecido")
        self.assertIn('Labrador desaparecido', html)
