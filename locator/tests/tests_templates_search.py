from django.urls import reverse
from unittest.mock import patch
from locator.tests.tests_base import LocatorTestBase


class LocatorTemplateSearch(LocatorTestBase):
    def test_template(self):
        response = self.client.get(reverse('search') + '?q=labrador')
        self.assertTemplateUsed(response, 'locator/pages/home.html')

    def test_404_status(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 404)

    def test_safety(self):
        response = self.client.get(reverse('search') + '?q=<virus>')
        self.assertIn('&lt;virus&gt;', response.content.decode('UTF8'))
        self.assertNotIn('<virus>', response.content.decode('UTF8'))

    def test_titles(self):
        author = self.makeAuthor()
        title1 = 'This is post one'
        title2 = 'This is post two'

        post1 = self.makePost(author=author, title=title1, slug='one')
        post2 = self.makePost(author=author, title=title2, slug='two')

        searchURL = reverse('search')
        response1 = self.client.get(f"{searchURL}?q={title1}")
        response2 = self.client.get(f"{searchURL}?q={title2}")
        responseTotal = self.client.get(f"{searchURL}?q=POST")

        self.assertIn(post1, response1.context['page'])
        self.assertNotIn(post2, response1.context['page'])

        self.assertIn(post2, response2.context['page'])
        self.assertNotIn(post1, response2.context['page'])

        self.assertIn(post1, responseTotal.context['page'])
        self.assertIn(post2, responseTotal.context['page'])

    def test_pagination(self):
        author = self.makeAuthor()
        title1 = 'This is post one'
        title2 = 'This is post two'
        title3 = 'This is post three'
        title4 = 'This is post four'
        title5 = 'This is post five'

        post1 = self.makePost(author=author, title=title1, slug='one')
        post2 = self.makePost(author=author, title=title2, slug='two')
        post3 = self.makePost(author=author, title=title3, slug='three')
        post4 = self.makePost(author=author, title=title4, slug='four')
        post5 = self.makePost(author=author, title=title5, slug='five')

        response = self.client.get(reverse('search') + "?q=POST")
        self.assertIn(post5, response.context['page'])
        self.assertIn(post4, response.context['page'])
        self.assertIn(post3, response.context['page'])
        self.assertIn(post2, response.context['page'])
        self.assertNotIn(post1, response.context['page'])

    def test_pagination_qty(self):
        author = self.makeAuthor()
        for i in range(8):
            kwargs = {'title': f'fake-title-{i}', 'slug': f'fake-slug-{i}', 'author': author}
            self.makePost(**kwargs)

        with patch('locator.views.QTY_PER_PAGE', new=3):
            response = self.client.get(reverse('search') + "?q=FAKE")
            paginationInfo = response.context['paginationInfo']
            paginator = paginationInfo.get('paginator')

            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)
