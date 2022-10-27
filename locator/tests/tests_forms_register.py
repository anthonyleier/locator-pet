from django.test import TestCase
from parameterized import parameterized
from locator.forms.register import RegisterForm
from django.urls import reverse


class LocatorFormsRegisterUnitTest(TestCase):
    @parameterized.expand([
        ('first_name', 'Ex.: João'),
        ('last_name', 'Ex.: Silva'),
        ('username', 'Ex.: joao.silva'),
        ('email', 'Ex.: joao.silva@gmail.com'),
        ('password', 'Sua senha'),
        ('password_confirm', 'Sua senha novamente'),
    ])
    def test_placeholders(self, field, placeholder):
        form = RegisterForm()
        currentPlaceholder = form[field].field.widget.attrs.get('placeholder')
        self.assertEqual(currentPlaceholder, placeholder)

    @parameterized.expand([
        ('username', 'Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.'),
        ('password', 'Necessário conter uma letra minúscula, uma letra maiúscula e um número. Tamanho mínimo de 8 caracteres.'),
    ])
    def test_helptexts(self, field, helptext):
        form = RegisterForm()
        currentHelpText = form[field].field.help_text
        self.assertEqual(currentHelpText, helptext)

    @parameterized.expand([
        ('first_name', 'Primeiro nome'),
        ('last_name', 'Último nome'),
        ('username', 'Usuário'),
        ('email', 'Email'),
        ('password', 'Senha'),
        ('password_confirm', 'Confirmação de senha'),
    ])
    def test_labels(self, field, label):
        form = RegisterForm()
        currentLabel = form[field].field.label
        self.assertEqual(currentLabel, label)


class LocatorFormsRegisterIntegrationTest(TestCase):
    def setUp(self):
        self.form_data = {
            'first_name': 'Nicolas',
            'last_name': 'Lopes',
            'username': 'nicolas.lopes',
            'email': 'nicolas.lopes@gmail.com',
            'password': 'Nico@2000',
            'password_confirm': 'Nico@2000',
        }

    @parameterized.expand([
        ('first_name', 'Primeiro nome não pode ser vazio.'),
        ('last_name', 'Último nome não pode ser vazio.'),
        ('username', 'Usuário não pode ser vazio.'),
        ('password', 'Senha não pode ser vazia.'),
        ('password_confirm', 'Confirmação de senha não pode ser vazia.'),
    ])
    def test_fields_cannot_be_empty(self, field, message):
        form_data = self.form_data
        form_data[field] = ''
        url = reverse('registerAction')
        response = self.client.post(url, data=form_data, follow=True)

        self.assertIn(message, response.content.decode('UTF8'))
        self.assertIn(message, response.context['form'].errors.get(field))

    def test_username_min_length(self):
        form_data = self.form_data
        form_data['username'] = 'ren'
        url = reverse('registerAction')
        response = self.client.post(url, data=form_data, follow=True)
        message = 'Usuário deve ter no mínimo 4 caracteres'

        self.assertIn(message, response.content.decode('UTF8'))
        self.assertIn(message, response.context['form'].errors.get('username'))

    def test_username_max_length(self):
        form_data = self.form_data
        form_data['username'] = 'ren' * 200
        url = reverse('registerAction')
        response = self.client.post(url, data=form_data, follow=True)
        message = 'Usuário deve ter no máximo 150 caracteres'

        self.assertIn(message, response.content.decode('UTF8'))
        self.assertIn(message, response.context['form'].errors.get('username'))

    def test_password_strong(self):
        form_data = self.form_data
        form_data['password'] = 'abc123'
        url = reverse('registerAction')
        response = self.client.post(url, data=form_data, follow=True)
        message = 'Sua senha é muito fraca.'

        self.assertIn(message, response.content.decode('UTF8'))
        self.assertIn(message, response.context['form'].errors.get('password'))

    def test_password_equals(self):
        form_data = self.form_data
        form_data['password'] = 'Abc@123'
        form_data['password_confirm'] = 'Abc@1234'

        url = reverse('registerAction')
        response = self.client.post(url, data=form_data, follow=True)
        message = 'As senhas devem ser iguais.'

        self.assertIn(message, response.content.decode('UTF8'))
        self.assertIn(message, response.context['form'].errors.get('password'))
        self.assertIn(message, response.context['form'].errors.get('password_confirm'))

    def test_get_form_404(self):
        url = reverse('registerAction')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_email_unique(self):
        form_data = self.form_data
        url = reverse('registerAction')
        message = 'Este email já está em uso.'

        self.client.post(url, data=form_data, follow=True)
        response = self.client.post(url, data=form_data, follow=True)

        self.assertIn(message, response.content.decode('UTF8'))
        self.assertIn(message, response.context['form'].errors.get('email'))

    def test_user_login(self):
        form_data = self.form_data
        url = reverse('registerAction')

        form_data.update({
            'username': 'nayara.lisboa',
            'password': 'Nay@2022',
            'password_confirm': 'Nay@2022'
        })
        self.client.post(url, data=form_data, follow=True)

        isAuthenticated = self.client.login(username='nayara.lisboa', password='Nay@2022')
        self.assertTrue(isAuthenticated)

        isAuthenticated = self.client.login(username='nayara.lisboa', password='Nay@2020')
        self.assertFalse(isAuthenticated)
