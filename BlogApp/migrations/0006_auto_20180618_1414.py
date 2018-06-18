# Generated by Django 2.1a1 on 2018-06-18 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0005_auto_20180618_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post_details', models.CharField(max_length=10000)),
                ('link', models.URLField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='post',
            new_name='post_details',
        ),
        migrations.AddField(
            model_name='postdetails',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogApp.BlogPost'),
        ),
    ]