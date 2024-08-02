from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = [
            (1298),
            (1098),
            (1098),
            (998),
            (998),
            (998),
        ]
        self.stdout.write("Создание пластиков")
        for plastic in plastics:
            type_ = TypePlastic.objects.get(name=plastic[0])
            color = ColorPlastic.objects.get(name=plastic[1])
            plastic, created = Plastic.objects.get_or_create(
                price=plastic[2],
                color=color,
                type=type_
            )
            if created:
                self.stdout.write(f"Пластик {plastic} создан")
            else:
                self.stdout.write(f"Пластик {plastic} уже был создан ранее")
