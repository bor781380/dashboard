# Generated by Django 5.0.6 on 2024-06-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0027_delete_shops_old'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversion',
            name='conversionFact',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
