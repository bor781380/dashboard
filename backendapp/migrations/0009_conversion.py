# Generated by Django 5.0.6 on 2024-06-15 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0008_rename_сhecks_checks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planFact', models.DecimalField(decimal_places=2, max_digits=5)),
                ('conversionFact', models.IntegerField()),
                ('APPG', models.DecimalField(decimal_places=2, max_digits=5)),
                ('shops', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendapp.shops')),
            ],
        ),
    ]
