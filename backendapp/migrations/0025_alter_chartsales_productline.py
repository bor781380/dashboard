# Generated by Django 5.0.6 on 2024-06-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0024_alter_chartsales_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartsales',
            name='productLine',
            field=models.CharField(default='Проверка', max_length=100),
        ),
    ]
