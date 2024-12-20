from django.core.management.base import BaseCommand
from django.utils.text import slugify
from movie.models import Production


class Command(BaseCommand):
    help = "Generate slugs for actors without slugs"

    def handle(self, *args, **kwargs):
        actors_without_slugs = Production.objects.filter(
            slug__isnull=True
            ) | Production.objects.filter(slug__exact="")
        updated_count = 0

        for actor in actors_without_slugs:
            actor.slug = slugify(actor.name)
            actor.save()
            updated_count += 1
            self.stdout.write(f"Updated slug for: {actor.name}")

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully updated {updated_count} actors' slugs.")
            )
