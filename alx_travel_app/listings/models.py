# listings/models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Listing(models.Model):
    """
    Represents a travel listing, like a hotel or vacation rental.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Using DecimalField is best practice for currency to avoid floating-point errors.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    
    # A listing is owned by a user. If the user is deleted, their listings are also deleted.
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    """
    Represents a booking made by a user for a specific listing.
    """
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.listing.title} by {self.guest.username}"

class Review(models.Model):
    """
    Represents a review left by a user for a listing.
    """
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    # Use validators to ensure the rating is between 1 and 5.
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.listing.title} by {self.user.username}"