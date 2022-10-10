from locator.models import Post
from parameterized import parameterized
from django.core.exceptions import ValidationError
from locator.tests.tests_base import LocatorTestBase


class LocatorModelsTest(LocatorTestBase):
    def setUp(self):
        self.author = self.makeAuthor()
        self.post = self.makePost(author=self.author)

    def test_post_title(self):
        self.post.title = '$' * 70

        with self.assertRaises(ValidationError):
            self.post.full_clean()  # Validation

    def test_post_fields_size(self):
        fields = [
            ('title', 65),
            ('description', 165),
            ('status', 15)
        ]

        for field, size in fields:
            with self.subTest(field=field, size=size):
                setattr(self.post, field, '$' * (size + 1))
                with self.assertRaises(ValidationError):
                    self.post.full_clean()  # Validation

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('status', 15)
    ])
    def test_post_fields_size_decorator(self, field, size):
        setattr(self.post, field, '$' * (size + 1))
        with self.assertRaises(ValidationError):
            self.post.full_clean()  # Validation

    def test_post_published_default(self):
        post = Post(
            title='Sumiu o poodle',
            description='Poodle fugiu na tarde de ontem',
            slug='sumiu-o-poodle',
            status='Encontrado',
            author=self.author)
        post.full_clean()  # Validation
        post.save()
        self.assertFalse(post.published)
