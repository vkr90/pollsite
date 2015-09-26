from django.contrib import admin

# Register your models here.
from polling.models import Polling, Hashtags

admin.site.register(Polling)
admin.site.register(Hashtags)