# Generated by Django 5.0.7 on 2024-08-29 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storestatus',
            name='store_id',
            field=models.CharField(max_length=255),
        ),
    ]
