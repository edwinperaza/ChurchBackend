from django.db import models

class Serie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='series', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


class Sermon(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    video_url = models.URLField(max_length=200)
    image_url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey('auth.User', related_name='sermons', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)