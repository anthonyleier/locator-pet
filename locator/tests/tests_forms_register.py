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
        ('username', 'Obraigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.'),
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
        ('email', 'Endereço de email'),
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
            'password2': 'Nico@2000',
        }

    @parameterized.expand([
        ('first_name', 'Primeiro nome não pode ser vazio.'),
        ('last_name', 'Último nome não pode ser vazio.'),
        ('username', 'Usuário não pode ser vazio.'),
        ('password', 'Senha não pode ser vazia.'),
        ('password_confirm', 'Confirmação de senha não pode ser vazia.'),
    ])
    def test_fields_cannot_be_empty(self, field, message):
        self.form_data[field] = ''
        url = reverse('registerAction')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertIn(message, response.content.decode('UTF8'))
        self.assertIn(message, response.context['form'].errors.get(field, ''))
        print(response.context['form'].errors.get(field, ''), field)


