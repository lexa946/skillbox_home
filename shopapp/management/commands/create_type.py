from django.core.management import BaseCommand
from shopapp.models import TypePlastic

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(f"Создание типа пластика {args[0]}")
        name = args[0]
        type_, created = TypePlastic.objects.get_or_create(name=name)
        if created:
            self.stdout.write(f"Тип {type_} создан")
        else:
            self.stdout.write(f"Тип {type_} уже был создан ранее")




    def add_arguments(self, parser):
        parser.add_argument(
            nargs="+",
            type=str,
            dest='args'
        )