from django.db import models

class Connect(models.Model):
    """Connect model"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    url_more_info = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)