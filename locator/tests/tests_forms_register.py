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
