from django.contrib import admin
from BlogApp.models import BlogPost, Comment


# BlogApp models
admin.site.register(BlogPost)
admin.site.register(Comment)

