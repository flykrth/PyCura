from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Profile, Patient, Doctor


class Command(BaseCommand):
    help = "Creates demo users: admin, doctor, patient"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating demo data...")

        # ---------------------
        # 1. Create admin user
        # ---------------------
        admin_user = User.objects.create_superuser(
            username="pandu",
            password="panduthegreat",
            first_name="Karthik"
        )
        Profile.objects.create(user=admin_user, role="admin")
        self.stdout.write(self.style.SUCCESS("✓ Admin user created (krth/krth)"))

