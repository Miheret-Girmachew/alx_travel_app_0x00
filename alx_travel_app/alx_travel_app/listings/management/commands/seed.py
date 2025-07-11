from django.core.management.base import BaseCommand

# Placeholder for the seeder command.
class Command(BaseCommand):
    help = 'Seeds the database with sample listings.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Database seeding placeholder...'))