# Generated by Django 2.1a1 on 2018-06-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Songs', '0007_auto_20180613_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=10000)),
            ],
        ),
    ]