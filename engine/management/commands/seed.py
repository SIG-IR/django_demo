from django.core.management import BaseCommand
from engine import seeder
class Command(BaseCommand):
    help = "Don't really need help here, just type the command"

    def handle(self, *args, **options):
        seeder.initialize()