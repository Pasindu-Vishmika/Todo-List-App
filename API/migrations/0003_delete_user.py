# Generated by Django 5.0.4 on 2024-04-24 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]