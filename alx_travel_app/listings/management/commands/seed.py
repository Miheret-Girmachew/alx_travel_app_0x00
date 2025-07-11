# listings/management/commands/seed.py

import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seeds the database with sample listings and users.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database seeding...')

        # --- Clean up existing data ---
        self.stdout.write('Deleting old data...')
        Listing.objects.all().delete()
        # Be careful not to delete superusers
        User.objects.filter(is_superuser=False).delete()

        # --- Create Sample Users ---
        self.stdout.write('Creating sample users...')
        users = []
        for i in range(5):
            username = f'user{i+1}'
            user = User.objects.create_user(username=username, password='password123', email=f'{username}@example.com')
            users.append(user)
        self.stdout.write(self.style.SUCCESS(f'{len(users)} users created.'))

        # --- Create Sample Listings ---
        self.stdout.write('Creating sample listings...')
        listings_data = [
            {'title': 'Cozy Beachfront Cottage', 'description': 'A beautiful cottage right on the beach.', 'price': 150.00, 'location': 'Malibu', 'country': 'USA'},
            {'title': 'Modern Downtown Loft', 'description': 'Stylish loft in the heart of the city.', 'price': 200.00, 'location': 'New York', 'country': 'USA'},
            {'title': 'Rustic Mountain Cabin', 'description': 'A quiet getaway in the mountains.', 'price': 100.00, 'location': 'Aspen', 'country': 'USA'},
            {'title': 'Charming Paris Apartment', 'description': 'An elegant apartment with a view of the Eiffel Tower.', 'price': 250.00, 'location': 'Paris', 'country': 'France'},
            {'title': 'Serene Lakeside Villa', 'description': 'A peaceful villa with a private lake.', 'price': 300.00, 'location': 'Lake Como', 'country': 'Italy'},
        ]

        created_listings = []
        for data in listings_data:
            # Assign a random owner from the users we created
            data['owner'] = random.choice(users)
            listing = Listing.objects.create(**data)
            created_listings.append(listing)
        
        self.stdout.write(self.style.SUCCESS(f'{len(created_listings)} listings created.'))
        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))