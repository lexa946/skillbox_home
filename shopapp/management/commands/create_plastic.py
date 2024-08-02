from django.core.management import BaseCommand
from shopapp.models import Plastic, ColorPlastic, TypePlastic, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        plastics = [
            ("PLA", "аллигатор", 1298, True),
            ("PLA", "анютины глазки", 1098, True),
            ("PLA", "белоснежка", 1098, True),
            ("PETG", "аватар", 998, True),
            ("PETG",  "белая гвардия", 998, False),
            ("PETG",  "васаби", 998, True),
        ]
        self.stdout.write("Создание пластиков")
        for plastic in plastics:

            type_ = TypePlastic.objects.get(name=plastic[0])
            color = ColorPlastic.objects.get(name=plastic[1])
            try:
                plastic = Plastic.objects.get(
                    color=color,
                    type=type_,
                )
                self.stdout.write(f"Пластик {plastic} уже был создан ранее")
            except Plastic.DoesNotExist:
                product = Product(price=plastic[2], discount=0, has_now=plastic[3])
                product.save()
                plastic = Plastic(
                    color=color,
                    type=type_,
                    product=product,
                )
                plastic.save()
                self.stdout.write(f"Пластик {plastic} создан")

