# Generated by Django 5.0.6 on 2024-06-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0018_alter_chartsales_planfact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartsales',
            name='planFact',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
    ]
