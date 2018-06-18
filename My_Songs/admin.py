from django.contrib import admin
from .models import Album, Song, BlogPost

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(BlogPost)