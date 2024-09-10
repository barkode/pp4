# Generated by Django 4.2.16 on 2024-09-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0003_alter_movie_options_movie_status_movie_updated_on"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movies",
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
                (
                    "title",
                    models.CharField(
                        max_length=200, unique=True, verbose_name="Movie Title"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        max_length=250,
                        null=True,
                        unique=True,
                        verbose_name="URL",
                    ),
                ),
                ("release_date", models.DateField()),
                ("sypnosis", models.TextField(max_length=400)),
                ("trailer", models.URLField(max_length=100)),
                ("info_link", models.URLField(max_length=100)),
                ("color_class", models.CharField(blank=True, max_length=20)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Published")], default=0
                    ),
                ),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Movie",
                "verbose_name_plural": "Movies",
                "db_table": "movie",
                "ordering": ["title"],
            },
        ),
    ]
