from django.urls import reverse
from django.test import TestCase


class LocatorUrls(TestCase):
    def test_home(self):
        url = reverse('locator:home')
        self.assertEqual(url, '/')

    def test_post(self):
        url = reverse('locator:post', args=[2])
        self.assertEqual(url, '/posts/2')

    def test_search(self):
        url = reverse('locator:search')
        self.assertEqual(url, '/posts/search')
