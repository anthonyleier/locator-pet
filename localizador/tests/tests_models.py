from localizador.tests.tests_base import LocalizadorTestBase
from django.core.exceptions import ValidationError


class LocalizadorModelsTest(LocalizadorTestBase):
    def setUp(self):
        self.post = self.criarPost()

    def test_post_titulo(self):
        self.post.titulo = '$' * 70

        with self.assertRaises(ValidationError):
            self.post.full_clean()
