# Generated by Django 4.1 on 2022-08-18 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_touristspot_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]
