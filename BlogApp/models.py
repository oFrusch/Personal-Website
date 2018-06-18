from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    post = models.CharField(max_length=10000)
    link = models.URLField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title


class SinglePost(models.Model):
    this_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post = models.CharField(max_length=10000)
    link = models.URLField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title
