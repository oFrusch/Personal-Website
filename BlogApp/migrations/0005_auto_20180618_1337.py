# Generated by Django 2.1a1 on 2018-06-18 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_auto_20180618_1336'),
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
