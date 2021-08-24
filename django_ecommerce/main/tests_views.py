from django.test import TestCase
from mixer.backend.django import mixer

from .models import Product


class TestHomeView(TestCase):

    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_context_home(self):
        response = self.client.get('/')
        self.assertIn('object_list', response.context)


class TestProductView(TestCase):

    def test_add_to_cart_button(self):
        mixer.blend(Product, img='media/vendors/apple-logo.jpg')

        response = self.client.get('/products/')
        self.assertIn(b'Add to Cart', response.content)
