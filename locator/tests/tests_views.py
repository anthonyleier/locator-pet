from locator import views
from django.test import TestCase
from django.urls import reverse, resolve


class LocatorViewsTest(TestCase):
    def test_home_view(self):
        view = resolve(reverse('locator:homepage'))
        self.assertIs(view.func, views.homepage)

    def test_post_view(self):
        view = resolve(reverse('locator:post', args=[2]))
        self.assertIs(view.func, views.post)

    def test_search_view(self):
        view = resolve(reverse('locator:search'))
        self.assertIs(view.func, views.search)
