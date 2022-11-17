import pytest
from locator.models import Post
from parameterized import parameterized
from django.core.exceptions import ValidationError
from locator.tests.tests_base import LocatorTestBase


@pytest.mark.fast
class LocatorModelsTest(LocatorTestBase):
    def setUp(self):
        self.user = self.makeUser()
        self.post = self.makePost(user=self.user)

    def test_post_title(self):
        self.post.title = '$' * 70

        with self.assertRaises(ValidationError):
            self.post.full_clean()

    def test_post_fields_size(self):
        fields = [('title', 65)]

        for field, size in fields:
            with self.subTest(field=field, size=size):
                setattr(self.post, field, '$' * (size + 1))
                with self.assertRaises(ValidationError):
                    self.post.full_clean()
                    self.post.save()

    @parameterized.expand([('title', 65)])
    def test_post_fields_size_decorator(self, field, size):
        setattr(self.post, field, '$' * (size + 1))
        with self.assertRaises(ValidationError):
            self.post.full_clean()
            self.post.save()

    def test_post_published_default(self):
        post = Post(
            title='Sumiu o poodle',
            description='Poodle fugiu na tarde de ontem',
            slug='sumiu-o-poodle',
            found=True,
            user=self.user)
        post.full_clean()
        post.save()
        self.assertFalse(post.published)
