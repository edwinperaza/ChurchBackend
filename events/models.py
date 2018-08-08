from django.db import models

# Create your models here.
class Event(models.Model):
    """Event model"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(max_length=200)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    address = models.CharField(max_length=200)
    url_more_info = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)