from django.core.management.base import BaseCommand
from dataentry.models import Student
import csv


# Proposed Command - python manage.py importdata filepath

class Command(BaseCommand):
    help = "Imports the data from a file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to CSV file")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"] # Get the name from the command line arguments
        print(file_path)
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Perform data validation and insertion here
                Student.objects.create(**row)
        self.stdout.write(self.style.SUCCESS("Data imported successfully from the CSB file"))

    