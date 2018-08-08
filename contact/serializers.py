"""Contact app serializer"""
from rest_framework import serializers
from django.contrib.auth.models import User
from contact.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    """Contact serializer"""
    class Meta:
        model = Contact
        fields = (
            'name',
            'slogan',
            'address',
            'main_pastor',
            'phone_number',
            'logo_url',
            'website_url',
            'facebook_url',
            'twitter_url',
            'instagram_url',
            'youtube_url',
            'snapchat_url',
            'created',
        )