# Generated by Django 4.1.5 on 2023-02-05 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_subscribe_options_remove_subscribe_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='is_check',
        ),
    ]