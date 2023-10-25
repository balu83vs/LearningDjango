from django.test import TestCase, Client
from django.urls import reverse
from .forms import UserRegForm
from .models import NoteUsers



class TestUserForm(TestCase):
    # тест формы
    def test_form(self):
        data = {
        'username':'test_user',
        'first_name':'test_firstname',
        'last_name':'test_lastname',
        'email':'test@test.ru',
        'password1':'admin12345',
        'password2':'admin12345'
        }

        test_form = UserRegForm(data=data)
        self.assertTrue(test_form.is_valid())


class TestModelForm(TestCase):
    # тест модели
    def setUp(self):
        NoteUsers.objects.create_user(
            username = 'testuser',
            first_name = 'testfn',
            last_name = 'testln',
            email = 'test@mail.ru'
        )

    def test_model_form(self):
        test_form = NoteUsers.objects.filter(username = 'testuser').first()
        self.assertEqual(test_form.username, 'testuser')
        self.assertEqual(test_form.first_name, 'testfn')
        self.assertEqual(test_form.last_name, 'testln')
        self.assertEqual(test_form.email, 'test@mail.ru')

    def tearDown(self):
        NoteUsers.objects.filter(username = 'testuser').delete()


class TestClientForm(TestCase):
    # тесты GET и POST запросов
    def test_get(self):
        client = Client()

        response = client.get(reverse('reg'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reg.html')

    def test_post(self):
        data = {
            'username': "testname",
            'first_name': 'test_fn',
            'last_name': 'test_ln',
            'email': 'test@email.ru',
            'password1': 'admin12345',
            'password2': 'admin12345'
        }    
        client = Client()

        response = client.post(reverse('reg'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        user = NoteUsers.objects.get(username='testname')
        self.assertEqual(user.first_name, 'test_fn')
        self.assertEqual(user.last_name, 'test_ln')
        self.assertEqual(user.email, 'test@email.ru')

