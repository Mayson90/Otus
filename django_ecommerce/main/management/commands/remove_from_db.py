from django.core.management.base import BaseCommand

from main.models import Category, Vendor, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Vendor.objects.all().delete()
        Product.objects.all().delete()

        print("[INFO]: Database was cleaned.")
