# Generated by Django 2.1a1 on 2018-06-18 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('My_Songs', '0010_artists'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Artists',
        ),
    ]