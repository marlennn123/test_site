# Generated by Django 5.1.4 on 2024-12-18 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_movielanguages_language_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.rating'),
        ),
    ]
