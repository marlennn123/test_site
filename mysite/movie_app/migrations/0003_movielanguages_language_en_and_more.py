# Generated by Django 5.1.4 on 2024-12-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_actor_actor_name_en_actor_actor_name_ru_actor_bio_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielanguages',
            name='language_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='movielanguages',
            name='language_ru',
            field=models.CharField(max_length=32, null=True),
        ),
    ]