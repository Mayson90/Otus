from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = get_user_model()

        # create superuser
        user.objects.create_superuser('admin', 'admin@mail.test', 'admin')
        print("[INFO]: Superuser was created: admin/admin.")
