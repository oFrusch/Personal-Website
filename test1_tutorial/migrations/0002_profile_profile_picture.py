# Generated by Django 2.1a1 on 2018-06-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1_tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]
