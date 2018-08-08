"""Contact app serializer"""
from rest_framework import serializers
from django.contrib.auth.models import User
from connects.models import Connect

class ConnectSerializer(serializers.ModelSerializer):
    """Contact serializer"""
    class Meta:
        model = Connect
        fields = (
            'title',
            'description',
            'phone_number',
            'address',
            'image_url',
            'url_more_info',
            'created',
        )