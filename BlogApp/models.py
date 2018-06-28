from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=10000)
    link = models.URLField(max_length=1000, null=True, blank=True)
    img = models.URLField(max_length=1000, null=True, blank=True)
    date_added = models.CharField(max_length=20, null=True, blank=True)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.title


