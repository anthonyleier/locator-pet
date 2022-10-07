from django.urls import reverse
from django.test import TestCase


class LocatorURLS(TestCase):
    def test_home_url(self):
        url = reverse('locator:homepage')
        self.assertEqual(url, '/')

    def test_post_url(self):
        url = reverse('locator:post', args=[2])
        self.assertEqual(url, '/posts/2')

    def test_post_search_url(self):
        url = reverse('locator:search')
        self.assertEqual(url, '/posts/search')
