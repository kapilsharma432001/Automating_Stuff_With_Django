from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = "Greets the user"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Specify the name of the user")
        

    def handle(self, *args, **kwargs):
        name = kwargs["name"]  # Get the name from the command-line arguments
        self.stdout.write(self.style.SUCCESS(f"Hi {name}!"))