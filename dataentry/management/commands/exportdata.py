from django.core.management.base import BaseCommand
from dataentry.models import Student
from django.apps import apps
from django.core.management import CommandError
import csv
import datetime



# Proposed command: python manage.py exportdata
class Command(BaseCommand):
    help = "Exports the data from the database to a CSV file"

    def handle(self, *args, **kwargs):
        # Fetch the data from the database
        students = Student.objects.all()

        # TimeStamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        # Define the csv file name and the path
        file_path = f'exported_students_data_{timestamp}.csv'
        print(file_path)

        # Open the csv file and write the data
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the csv header
            writer.writerow(['Roll No', 'Name', 'Age'])

            # Write data rows
            for student in students:
                writer.writerow([student.roll_no, student.name, student.age])

            
        self.stdout.write(self.style.SUCCESS('Data exported successfully !!'))
            
