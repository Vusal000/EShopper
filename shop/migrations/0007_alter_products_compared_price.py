# Generated by Django 4.1.5 on 2023-02-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_products_compared_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='compared_price',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
    ]
