import json
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from movie.models import Movie, Actor, Genre, Rating, Production


class Command(BaseCommand):
    help = 'Imports movie data from a JSON file into the database with slugs'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the JSON file')

    def validate_item(self, item):
        """
        Validate a record from JSON.
        """
        errors = []

        # Validate 'Title'
        if 'Title' not in item or not item['Title']:
            errors.append("Title is missing or empty.")

        # Validate 'Plot'
        if 'Plot' not in item or not item['Plot']:
            errors.append("Plot is missing or empty.")

        # Add more validation rules as needed

        if errors:
            raise ValidationError(errors)

    def generate_unique_slug(self, title):
        """
        Generate a unique slug based on the title.
        """
        original_slug = slugify(title)
        queryset = Movie.objects.filter(slug=original_slug)
        unique_slug = original_slug
        counter = 1

        while queryset.exists():
            unique_slug = f"{original_slug}-{counter}"
            counter += 1
            queryset = Movie.objects.filter(slug=unique_slug)

        return unique_slug

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        # Open JSON file
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File {file_path} not found"))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f"Error decoding JSON in file {file_path}"))
            return

        valid_objects = []
        invalid_count = 0

        # Prepare for bulk creation
        for item in data:
            try:
                self.validate_item(item)

                # Handle production
                production_name = item.get('Production', None)
                production, _ = Production.objects.get_or_create(name=production_name)

                # Create movie object
                movie = Movie(
                    title=item['Title'],
                    year=item.get('Year', ''),
                    rated=item.get('Rated', ''),
                    released=item.get('Released', ''),
                    runtime=item.get('Runtime', ''),
                    plot=item['Plot'],
                    language=item.get('Language', ''),
                    country=item.get('Country', ''),
                    awards=item.get('Awards', ''),
                    poster=item.get('Poster', ''),
                    metascore=item.get('Metascore', ''),
                    imdb_rating=item.get('imdbRating', ''),
                    imdb_votes=item.get('imdbVotes', ''),
                    imdb_id=item.get('imdbID', ''),
                    type=item.get('Type', ''),
                    dvd=item.get('DVD', ''),
                    box_office=item.get('BoxOffice', ''),
                    production=production,
                    website=item.get('Website', ''),
                    slug=self.generate_unique_slug(item['Title']),
                    )

                # Save movie object to get an id for many-to-many relationships
                movie.save()

                # Handle actors
                actor_names = [name.strip() for name in item.get('Actors', '').split(',')]
                for actor_name in actor_names:
                    actor, _ = Actor.objects.get_or_create(name=actor_name)
                    movie.actors.add(actor)

                # Handle genres
                genre_names = [name.strip() for name in item.get('Genre', '').split(',')]
                for genre_name in genre_names:
                    genre, _ = Genre.objects.get_or_create(name=genre_name)
                    movie.genres.add(genre)

                # Handle ratings
                ratings = item.get('Ratings', [])
                for rating in ratings:
                    Rating.objects.create(
                        movie=movie,
                        source=rating.get('Source', ''),
                        value=rating.get('Value', '')
                        )

                valid_objects.append(movie)

            except ValidationError as e:
                self.stdout.write(self.style.ERROR(f"Invalid data: {item} - {e}"))
                invalid_count += 1

        # Perform bulk_create if there are valid objects
        if valid_objects:
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(valid_objects)} records"))
        else:
            self.stdout.write(self.style.WARNING("No valid data to import"))

        if invalid_count > 0:
            self.stdout.write(self.style.WARNING(f"Skipped {invalid_count} invalid records"))
