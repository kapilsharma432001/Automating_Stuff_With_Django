from django.core.management.base import BaseCommand
from dataentry.models import Student
from django.apps import apps
from django.core.management import CommandError
import csv


# Proposed Command - python manage.py importdata filepath model_name 

class Command(BaseCommand):
    help = "Imports the data from a file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to CSV file")
        parser.add_argument("model_name", type=str, help="Name of the model")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"] # Get the file path from the command line arguments
        model_name = kwargs["model_name"].capitalize() # Get the model name from the command line arguments
        print(file_path)

        # Search for the model (model_name which user is specifying) across all the installed apps
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name=model_name)
                break # If the model is found, break the loop

            except LookupError:
                continue # model not found in this app, continue searching in the next app

        if not model:
            raise CommandError(f"Model {model_name} not found")

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Perform data validation and insertion here
                Student.objects.create(**row)
        self.stdout.write(self.style.SUCCESS("Data imported successfully from the CSV file"))

    