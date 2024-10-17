from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = "This command is used to insert data into the database"

    def handle(self, *args, **kwargs):
        # Inserting 1 data
        dataset = [
            {"roll_no": 102, "name": "XYZ", "age": 24},
            {"roll_no": 103, "name": "BCD", "age": 25},
            {"roll_no": 104, "name": "EFG", "age": 26},
        ]

        for data in dataset:
            roll_no = data["roll_no"]
            existing_record = Student.objects.filter(roll_no=roll_no).exists()

            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
                self.stdout.write(self.style.SUCCESS(f"Data inserted successfully for roll no {roll_no}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Student with roll no {roll_no} already exists in the database"))
        
        
