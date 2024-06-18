# Generated by Django 5.0.6 on 2024-06-15 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0011_alter_specialtask_shops'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialtask',
            name='shops',
        ),
        migrations.CreateModel(
            name='SpecialTask_old',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('planFact', models.DecimalField(decimal_places=2, max_digits=5)),
                ('shops', models.ManyToManyField(related_name='special_tasks', to='backendapp.shops')),
            ],
        ),
        migrations.AddField(
            model_name='specialtask',
            name='shops',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='backendapp.shops'),
            preserve_default=False,
        ),
    ]