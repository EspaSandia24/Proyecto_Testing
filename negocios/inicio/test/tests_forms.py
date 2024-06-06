
from inicio.forms import UserForm
from django.test import TestCase
from django.contrib.auth.models import User


class UserFormTest(TestCase):

    def test_user_form_valid(self):
        form = UserForm(data={
            'username': 'usuario',
            'email': 'usuario@example.com',
            'password': 'password123',
            're_pass': 'password123'
        })
        self.assertTrue(form.is_valid())

    def test_user_form_invalid_password_mismatch(self):
        form = UserForm(data={
            'username': 'usuario',
            'email': 'usuario@example.com',
            'password': 'password123',
            're_pass': 'password456'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [
                         'Las contraseñas no son iguales'])

    def test_user_form_save(self):
        form = UserForm(data={
            'username': 'usuario',
            'email': 'usuario@example.com',
            'password': 'password123',
            're_pass': 'password123'
        })
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'usuario')
        self.assertTrue(user.check_password('password123'))

    def test_user_form_save_with_commit_false(self):
        form = UserForm(data={
            'username': 'usuario',
            'email': 'usuario@example.com',
            'password': 'password123',
            're_pass': 'password123'
        })
        self.assertTrue(form.is_valid())
        user = form.save(commit=False)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'usuario')
        self.assertTrue(user.check_password('password123'))
        # El usuario aún no se ha guardado en la base de datos
        self.assertIsNone(user.id)
        user.save()
        # El usuario ahora está guardado en la base de datos
        self.assertIsNotNone(user.id)
