from django.contrib import admin

# Register your models here.
from .models import Sermon
from .models import Serie

#admin.site.register(Serie)
#admin.site.register(Sermon)

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'pastor_name', 'date','video_url')

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin): 
    list_display = ('title','image_url')