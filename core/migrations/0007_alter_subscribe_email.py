# Generated by Django 4.1.5 on 2023-02-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(db_index=True, max_length=100, unique=True),
        ),
    ]