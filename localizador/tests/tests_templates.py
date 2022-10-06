from django.urls import reverse
from localizador.tests.tests_base import LocalizadorTestBase


class LocalizadorTemplatesTest(LocalizadorTestBase):
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
        self.criarPost()
        response = self.client.get(reverse('localizador:homepage'))
        html = response.content.decode('UTF8')

        self.assertEqual(len(response.context['posts']), 1)
        self.assertEqual(response.context['posts'].first().titulo, "Labrador desaparecido")
        self.assertIn('Labrador desaparecido', html)
        self.limparPosts()

    def test_post_detalhes(self):
        post = self.criarPost()
        response = self.client.get(reverse('localizador:post', args=[post.id]))
        html = response.content.decode('UTF8')

        self.assertEqual(response.context['post'].titulo, "Labrador desaparecido")
        self.assertIn('Labrador desaparecido', html)
        self.limparPosts()

    def test_home_nao_publicado(self):
        self.criarPost(publicado=False)
        response = self.client.get(reverse('localizador:homepage'))
        self.assertIn('Nenhum post cadastrado', response.content.decode('UTF8'))
        self.limparPosts()

    def test_post_nao_publicado(self):
        post = self.criarPost(publicado=False)
        response = self.client.get(reverse('localizador:post', args=[post.id]))
        self.assertEqual(response.status_code, 404)
        self.limparPosts()

    def test_search_template(self):
        response = self.client.get(reverse('localizador:search') + '?q=labrador')
        self.assertTemplateUsed(response, 'localizador/pages/search.html')

    def test_search_404(self):
        response = self.client.get(reverse('localizador:search'))
        self.assertEqual(response.status_code, 404)

    def test_search_seguranca_template(self):
        response = self.client.get(reverse('localizador:search') + '?q=<scriptmalicioso>')
        self.assertIn('&lt;scriptmalicioso&gt;', response.content.decode('UTF8'))
        self.assertNotIn('<scriptmalicioso>', response.content.decode('UTF8'))

    def test_search_titulo(self):
        titulo1 = 'Este é o post 1'
        titulo2 = 'Este é o post 2'

        post1 = self.criarPost(titulo=titulo1, slug='um')
        post2 = self.criarPost(titulo=titulo2, slug='dois')

        searchURL = reverse('localizador:search')
        response1 = self.client.get(f"{searchURL}?q={titulo1}")
        response2 = self.client.get(f"{searchURL}?q={titulo2}")
        responseTotal = self.client.get(f"{searchURL}?q=POST")

        self.assertIn(post1, response1.context['posts'])
        self.assertNotIn(post2, response1.context['posts'])

        self.assertIn(post2, response2.context['posts'])
        self.assertNotIn(post1, response2.context['posts'])

        self.assertIn(post1, responseTotal.context['posts'])
        self.assertIn(post2, responseTotal.context['posts'])
