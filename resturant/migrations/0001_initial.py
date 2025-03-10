# Generated by Django 5.1.5 on 2025-02-04 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resturant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=200)),
                ('phone_number', models.CharField(blank=True, max_length=14, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('resturant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tables', to='resturant.resturant')),
            ],
        ),
    ]
