from localizador import views
from django.test import TestCase
from django.urls import reverse, resolve


class LocalizadorViewsTest(TestCase):
    def test_home_view(self):
        view = resolve(reverse('localizador:homepage'))
        self.assertIs(view.func, views.homepage)

    def test_post_view(self):
        view = resolve(reverse('localizador:post', args=[2]))
        self.assertIs(view.func, views.post)
