# Generated by Django 2.1a1 on 2018-06-13 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Songs', '0006_remove_song_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_description',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='song_description',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
