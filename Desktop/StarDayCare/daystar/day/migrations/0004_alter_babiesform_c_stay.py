# Generated by Django 5.0.4 on 2024-05-16 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0003_alter_babiesform_c_stay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babiesform',
            name='c_stay',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='day.categorystay'),
        ),
    ]
