from django.core.management.base import BaseCommand

from main.models import Category, Vendor, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Category.objects.count() == 0:
            # creation Categories
            laptops = Category.objects.create(name='Laptops')
            desktops = Category.objects.create(name='Desktops')
            monitors = Category.objects.create(name='Monitors')
            accessories = Category.objects.create(name='Accessories')
        else:
            print("[WARNING]: Category objects already exists.")

        if Vendor.objects.count() == 0:
            # creation Vendors
            apple = Vendor.objects.create(name='Apple', img='vendors/apple-logo.jpg')
            lenovo = Vendor.objects.create(name='Lenovo', img='vendors/lenovo-logo.png')
            xiaomi = Vendor.objects.create(name='Xiaomi', img='vendors/xiaomi-logo.png')
            dell = Vendor.objects.create(name='Dell', img='vendors/dell-logo.jpg')
            logitech = Vendor.objects.create(name='Logitech', img='vendors/logitech-logo.png')
            adam = Vendor.objects.create(name='Adam', img='vendors/adam-logo.png')
        else:
            print("[WARNING]: Vendor objects already exists.")

        if Product.objects.count() == 0:
            # creation Products
            product1 = Product.objects.create(
                name='Macbook Pro 15',
                category=laptops,
                vendor=apple,
                cost=1899,
                img='products/macbook-pro-15.jpeg'
            )
            product2 = Product.objects.create(
                name='Mac Pro',
                category=desktops,
                vendor=apple,
                cost=4109,
                img='products/mac-pro.jpg'
            )
            product3 = Product.objects.create(
                name='ThinkPad P17',
                category=laptops,
                vendor=lenovo,
                cost=1299,
                img='products/thinkpad-p17.jpg'
            )
            product4 = Product.objects.create(
                name='ThinkCentre M90q',
                category=desktops,
                vendor=lenovo,
                cost=899,
                img='products/thinkcentre-m90q.webp'
            )
            product5 = Product.objects.create(
                name='Mi Notebook Pro 15',
                category=laptops,
                vendor=xiaomi,
                cost=1399,
                img='products/xiaomi-mi-notebook-pro-15.jpg'
            )
            product6 = Product.objects.create(
                name='AlienWare 38',
                category=monitors,
                vendor=dell,
                cost=799,
                img='products/dell-alienware-38.jpg'
            )
            product7 = Product.objects.create(
                name='Audio A7X',
                category=accessories,
                vendor=adam,
                cost=589,
                img='products/adam-a7x.jpeg'
            )
            product8 = Product.objects.create(
                name='Mouse G604',
                category=accessories,
                vendor=logitech,
                cost=80,
                img='products/logitech-g604.jpeg'
            )
        else:
            print("[WARNING]: Product objects already exists.")

        print("[INFO]: Database was filled.")
