from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email="admin1@admin.com",
            first_name="Admin",
            last_name="Admin",
            is_active=True,
            is_superuser=True,
            is_staff=True,
        )

        user.set_password("123456")
        user.save()
