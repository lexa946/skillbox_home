from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Product, Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = Product.objects.all()
        user = User.objects.get(username="admin")
        self.stdout.write("Создание заказа")
        order, created = Order.objects.get_or_create(
            user=user,
            delivery_address="Московское шоссе д. 28 кв 137",
            promocode="WTF",
        )
        if created:
            for product in products:
                order.products.add(product)
            self.stdout.write(f"Заказ {order} создан")
        else:
            self.stdout.write(f"Заказ {order} уже был создан ранее")


        # for plastic in plastics:


