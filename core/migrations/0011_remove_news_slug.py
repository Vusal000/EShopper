# Generated by Django 4.1.5 on 2023-02-18 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_news_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='slug',
        ),
    ]
