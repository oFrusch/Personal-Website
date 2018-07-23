from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=10000)
    link = models.URLField(max_length=1000, null=True, blank=True)
    img = models.URLField(max_length=1000, null=True, blank=True)
    date_added = models.CharField(max_length=20, null=True, blank=True)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, null=True, on_delete=models.CASCADE)  # Relates Comment with BlogPost
    commenter = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField('Date Posted', default=timezone.now)
    comment = models.TextField(max_length=2000)

    def get_absolute_url(self):
        return reverse('BlogApp:all_posts')

    def __str__(self):
        return self.comment





