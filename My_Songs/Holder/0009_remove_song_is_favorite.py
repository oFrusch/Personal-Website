# Generated by Django 2.1a1 on 2018-06-07 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('My_Songs', '0008_song_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='is_favorite',
        ),
    ]
