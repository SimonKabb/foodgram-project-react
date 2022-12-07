import csv

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def load_titles(self):
        from recipes.models import Ingredient
        with open(r'static\data\titles.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                ingredient = Ingredient(
                    name=row[0], measurement_unit=row[1]
                )
                ingredient.save()

    def handle(self, *args, **options):
        self.load_titles()
