# Generated by Django 5.0.6 on 2024-06-15 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0003_shops_old_remove_shops_conversion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traffic',
            old_name='сount',
            new_name='count',
        ),
    ]
