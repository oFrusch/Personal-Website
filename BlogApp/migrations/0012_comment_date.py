# Generated by Django 2.1a1 on 2018-07-23 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Posted'),
        ),
    ]
