"""Sermon app serializer"""
from rest_framework import serializers
from django.contrib.auth.models import User
from sermons.models import Serie, Sermon

class SerieSerializer(serializers.ModelSerializer):
    """Serie serializer"""
    class Meta:
        model = Serie
        fields = (
            'title',
            'description',
            'image_url',
            'created',
        )


class SermonSerializer(serializers.ModelSerializer):
    """Sermon serializer"""
    class Meta:
        model = Sermon
        fields = (
            'serie',
            'title',
            'pastor_name',
            'description',
            'video_url',
            'image_url',
            'date',
            'created',
        )

class UserSerializer(serializers.ModelSerializer):
    """User serializer"""
    #series = serializers.PrimaryKeyRelatedField(many=True, queryset=Serie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username')
        #fields = ('id', 'username', 'series')
