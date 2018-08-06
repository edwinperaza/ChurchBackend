from rest_framework import serializers
from sermons.models import Serie, Sermon
from django.contrib.auth.models import User

class SerieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Serie
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = (
            'title',
            'description',
            'image_url',
            'created',
        )


class SermonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sermon
        #owner = serializers.ReadOnlyField(source='owner.username')
        fields = (
            'serie',
            'title',
            'description',
            'video_url',
            'image_url',
            'created',
        )

class UserSerializer(serializers.ModelSerializer):
    series = serializers.PrimaryKeyRelatedField(many=True, queryset=Serie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'series')