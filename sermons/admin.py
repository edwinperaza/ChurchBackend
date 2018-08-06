from django.contrib import admin

# Register your models here.
from .models import Sermon
from .models import Serie

admin.site.register(Serie)
admin.site.register(Sermon)