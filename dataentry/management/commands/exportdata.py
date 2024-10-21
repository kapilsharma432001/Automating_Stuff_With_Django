from django.core.management.base import BaseCommand
from dataentry.models import Student
from django.apps import apps
from django.core.management import CommandError
import csv
import datetime



# Proposed command: python manage.py exportdata model_name
class Command(BaseCommand):
    help = "Export the data from a model (specified by the user) to a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("model_name", type=str, help="Name of the model")

    def handle(self, *args, **kwargs):

        model_name = kwargs["model_name"].capitalize()

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

        # Fetch the data from the database
        data = model.objects.all()

        # TimeStamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        # Define the csv file name and the path
        file_path = f'exported_{model_name}_data_{timestamp}.csv'
        print(file_path)

        # Open the csv file and write the data
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the csv header
            # Writing the header of the excel file according to the fields present in the model
            writer.writerow([field.name for field in model._meta.fields])

            # Write data rows
            for dt in data:
                writer.writerow([ getattr(dt, field.name) for field in model._meta.fields])

            
        self.stdout.write(self.style.SUCCESS('Data exported successfully !!'))
            
