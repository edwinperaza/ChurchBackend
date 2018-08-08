from django.db import models

# Create your models here.
class Contact(models.Model):
    """Contact model"""
    name = models.CharField(max_length=200)
    slogan = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    main_pastor = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    logo_url = models.URLField(max_length=200)
    website_url = models.URLField(max_length=200)
    facebook_url = models.URLField(max_length=200)
    twitter_url = models.URLField(max_length=200)
    instagram_url = models.URLField(max_length=200)
    youtube_url = models.URLField(max_length=200)
    snapchat_url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)