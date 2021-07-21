from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .models import Category, Vendor, Product


class TestCategory(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Laptop')

    def tearDown(self):
        print('clean up')

    def test_create(self):
        self.assertEqual(self.category.name, 'Laptop')

    def test_str(self):
        self.assertEqual(str(self.category), 'Laptop')


class TestVendor(TestCase):

    def setUp(self):
        self.vendor = Vendor.objects.create(name='Apple')
        self.image = Vendor.objects.count()

    def tearDown(self):
        print('clean up')

    def test_create(self):
        self.assertEqual(self.vendor.name, 'Apple')

    def test_str(self):
        self.assertEqual(str(self.vendor), 'Apple')

    def test_img_upload(self):
        img = Vendor()
        img_path = 'media/vendors/apple-logo.jpg'
        img.image = SimpleUploadedFile(name='apple-logo.jpg', content=open(img_path, 'rb').read())
        img.save()
        self.assertEqual(self.image, 1)


class TestProduct(TestCase):

    def setUp(self):
        self.product = Product.objects.create(cost=123)

    def tearDown(self):
        print('clean up')

    def test_create_cost(self):
        self.assertTrue(self.product.cost)
