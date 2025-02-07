# Generated by Django 5.1.5 on 2025-02-05 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0003_restaurant_alter_table_resturant'),
        ('user', '0002_user_resturant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='resturant',
        ),
        migrations.AddField(
            model_name='user',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resturant.restaurant'),
        ),
    ]
