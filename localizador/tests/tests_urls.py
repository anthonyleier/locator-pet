from django.urls import reverse
from django.test import TestCase


class LocalizadorURLS(TestCase):
    def test_home_url(self):
        url = reverse('localizador:homepage')
        self.assertEqual(url, '/')

    def test_post_url(self):
        url = reverse('localizador:post', args=[2])
        self.assertEqual(url, '/posts/2')
