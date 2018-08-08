"""Sermon app serializer"""
from rest_framework import serializers
from django.contrib.auth.models import User
from events.models import Event

class EventSerializer(serializers.ModelSerializer):
    """Serie serializer"""
    class Meta:
        model = Event
        fields = (
            'title',
            'description',
            'image_url',
            'date_start',
            'date_end',
            'address',
            'url_more_info',
            'created',
        )