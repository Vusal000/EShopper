# Generated by Django 4.1.5 on 2023-02-09 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_news_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
    ]
