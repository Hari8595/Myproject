# Generated by Django 4.2.2 on 2023-06-24 05:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movies_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
