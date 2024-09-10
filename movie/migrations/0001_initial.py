# Generated by Django 4.2.16 on 2024-09-10 09:25

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("release_date", models.DateField()),
                (
                    "poster",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="image"
                    ),
                ),
                ("sypnosis", models.TextField(max_length=400)),
                ("trailer", models.URLField(max_length=100)),
                ("info_link", models.URLField(max_length=100)),
                ("color_class", models.CharField(blank=True, max_length=20)),
            ],
            options={
                "verbose_name": "Movie",
                "verbose_name_plural": "Movies",
                "db_table": "movie",
            },
        ),
    ]