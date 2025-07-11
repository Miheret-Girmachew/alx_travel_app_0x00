# listings/serializers.py

from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    """
    class Meta:
        model = Listing
        # '__all__' includes all fields from the model in the serialization.
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    """
    class Meta:
        model = Booking
        fields = '__all__'