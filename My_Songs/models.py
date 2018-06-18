from django.db import models

# Sets up DB entries/structure


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.CharField(max_length=1000)
    album_description = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.album_title + ' by ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # Relates albums and songs
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    song_link = models.CharField(max_length=1000, null=True, blank=True)
    song_description = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.song_title



