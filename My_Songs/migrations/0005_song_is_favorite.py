# Generated by Django 2.1a1 on 2018-06-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Songs', '0004_remove_song_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
