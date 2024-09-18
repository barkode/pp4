import json
from django.core.management.base import BaseCommand
from movie.models import Movie
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class Command(BaseCommand):
    help = 'Imports movie data from a JSON file into the database with slugs'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the JSON file')

    def validate_item(self, item):
        """
        Validating records from JSON.
        """
        errors = []

        # Validate 'Title'
        if 'Title' not in item or not item['Title']:
            errors.append("Title is missing or empty.")

        # Validate 'Plot'
        if 'Plot' not in item or not item['Plot']:
            errors.append("Plot is missing or empty.")

        if errors:
            raise ValidationError(errors)

    def generate_unique_slug(self, title):
        """
        Generation of a unique slug based on the title field.
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

        # Open the JSON file
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

        # Validation of data and preparation of objects for bulk_create
        for item in data:
            try:
                self.validate_item(item)
                valid_objects.append(
                    Movie(
                        title=item['Title'],  # Use 'Title' from JSON
                        plot=item['Plot'],  # Use 'Plot' from JSON
                        slug=self.generate_unique_slug(item["Title"]),
                        )
                    )
            except ValidationError as e:
                self.stdout.write(self.style.ERROR(f"Invalid data: {item} - {e}"))
                invalid_count += 1

        # If there are valid objects, we execute bulk_create
        if valid_objects:
            Movie.objects.bulk_create(valid_objects)
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(valid_objects)} records"))
        else:
            self.stdout.write(self.style.WARNING("No valid data to import"))

        if invalid_count > 0:
            self.stdout.write(self.style.WARNING(f"Skipped {invalid_count} invalid records"))
