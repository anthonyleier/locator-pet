from locator.models import Post
from django.test import TestCase
from django.contrib.auth.models import User


class LocatorTestBase(TestCase):
    def makeUser(
            self,
            first_name="Julio",
            last_name="Santos",
            username="julio.santos",
            password="alfa@2020",
            email="julio.santos@alfatransportes.com.br"):

        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email)

    def makePost(
            self,
            title='Não consigo encontrar o meu doberman',
            description='Doberman está desaparecido desde o dia de ontem',
            slug='nao-consigo-encontrar-o-meu-doberman',
            found=False,
            published=True,
            image1='locator/upload/2022/10/10/doberman.jpg',
            user=None):

        if not user:
            user = self.makeUser()

        return Post.objects.create(
            title=title,
            description=description,
            slug=slug,
            found=found,
            published=published,
            image1=image1,
            user=user)
