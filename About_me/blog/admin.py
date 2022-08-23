from django.contrib import admin

# Register your models here.
from .models import Articles, Like

admin.site.register(Articles)
admin.site.register(Like)
