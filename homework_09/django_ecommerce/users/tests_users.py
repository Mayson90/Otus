from django.test import TestCase

from users.models import NewUser


class TestUserAuth(TestCase):

    def test_admin_auth(self):
        login = 'admin'
        password = 'Qwerty123456'
        NewUser.objects.create_superuser(username=login, email='admin@testmail.com', password=password)

        self.client.login(username=login, password=password)

        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

        self.client.logout()

    def test_user_auth(self):
        login = 'Andrey'
        password = 'Qwerty123456'
        NewUser.objects.create_user(username=login, email='andrey@testmail.com', password=password)

        self.client.login(username=login, password=password)

        response = self.client.get('/admin/')
        self.assertNotEqual(response.status_code, 200)

        self.client.logout()
