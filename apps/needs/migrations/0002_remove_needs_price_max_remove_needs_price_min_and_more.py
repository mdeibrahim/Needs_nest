# Generated by Django 5.2.4 on 2025-07-13 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('needs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='needs',
            name='price_max',
        ),
        migrations.RemoveField(
            model_name='needs',
            name='price_min',
        ),
        migrations.RemoveField(
            model_name='needs',
            name='sub_category',
        ),
    ]
