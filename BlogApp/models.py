from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    post = models.CharField(max_length=10000)

    def __str__(self):
        return self.title
