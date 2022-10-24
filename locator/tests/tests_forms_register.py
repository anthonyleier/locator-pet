from django.test import TestCase
from locator.forms import RegisterForm
from parameterized import parameterized


class LocatorFormsRegister(TestCase):
    @parameterized.expand([
        ('first_name', 'Ex.: John'),
        ('last_name', 'Ex.: Smith'),
        ('username', 'Ex.: jonh.smith'),
        ('email', 'Ex.: jonh.smith@gmail.com'),
        ('password', 'Your password'),
        ('password_confirm', 'Your password again'),
    ])
    def test_placeholders(self, field, placeholder):
        form = RegisterForm()
        currentPlaceholder = form[field].field.widget.attrs.get('placeholder')
        self.assertEqual(currentPlaceholder, placeholder)

    @parameterized.expand([
        ('password', 'Password must have at least one uppercase letter, one lowercase letter and one number. The length should be at least 8 characters.'),
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
        ('password', 'Password'),
        ('password_confirm', 'Password confirm'),
    ])
    def test_labels(self, field, label):
        form = RegisterForm()
        currentLabel = form[field].field.label
        self.assertEqual(currentLabel, label)
