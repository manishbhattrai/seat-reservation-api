# Generated by Django 5.1.5 on 2025-02-10 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
        ('resturant', '0009_restaurant_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='resturant.restaurant'),
        ),
    ]
