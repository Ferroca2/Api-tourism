# Generated by Django 4.1 on 2022-08-15 00:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_touristspot_avaliations_touristspot_comments'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('avaliations', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avaliations',
            new_name='Avaliation',
        ),
    ]