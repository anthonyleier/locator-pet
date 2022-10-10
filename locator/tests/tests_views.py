from locator import views
from django.test import TestCase
from django.urls import reverse, resolve


class LocatorViews(TestCase):
    def test_home(self):
        view = resolve(reverse('locator:home'))
        self.assertIs(view.func, views.home)

    def test_post(self):
        view = resolve(reverse('locator:post', args=[2]))
        self.assertIs(view.func, views.post)

    def test_search(self):
        view = resolve(reverse('locator:search'))
        self.assertIs(view.func, views.search)
