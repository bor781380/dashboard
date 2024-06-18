# Generated by Django 5.0.6 on 2024-06-15 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0014_productline_balancesname_productline_colorname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartsales',
            name='planFact',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.RemoveField(
            model_name='chartsales',
            name='shops',
        ),
        migrations.AddField(
            model_name='chartsales',
            name='shops',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='backendapp.shops'),
            preserve_default=False,
        ),
    ]