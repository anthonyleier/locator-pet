from django.urls import reverse
from locator.tests.tests_base import LocatorTestBase


class LocatorTemplatePost(LocatorTestBase):
    def test_template(self):
        post = self.makePost()
        response = self.client.get(reverse('post', args=[post.id]))
        self.assertTemplateUsed(response, 'locator/pages/post.html')

    def test_404_status(self):
        response = self.client.get(reverse('post', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_details(self):
        post = self.makePost()
        response = self.client.get(reverse('post', args=[post.id]))
        html = response.content.decode('UTF8')

        self.assertEqual(response.context['post'].title, "Não consigo encontrar o meu doberman")
        self.assertIn('Não consigo encontrar o meu doberman', html)

    def test_not_published(self):
        post = self.makePost(published=False)
        response = self.client.get(reverse('post', args=[post.id]))
        self.assertEqual(response.status_code, 404)
