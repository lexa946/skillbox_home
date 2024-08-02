from django.core.management import BaseCommand
from shopapp.models import ColorPlastic

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(f"Создание цвета пластика {args[0]} | {args[1]}")
        name, hex = args
        color, created = ColorPlastic.objects.get_or_create(name=name, hex=hex)
        if created:
            self.stdout.write(f"Цвет {color} создан")
        else:
            self.stdout.write(f"Цвет {color} уже был создан ранее")




    def add_arguments(self, parser):
        parser.add_argument(
            nargs="+",
            type=str,
            dest='args'
        )