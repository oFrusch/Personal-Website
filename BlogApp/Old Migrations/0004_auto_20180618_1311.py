# Generated by Django 2.1a1 on 2018-06-18 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0003_singlepost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singlepost',
            name='this_post',
        ),
        migrations.DeleteModel(
            name='SinglePost',
        ),
    ]