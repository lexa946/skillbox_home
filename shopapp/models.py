from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


# Create your models here.

class NameProductProperty(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class ValueProductProperty(models.Model):
    value = models.TextField(null=False, blank=False)

    def __str__(self):
        if len(self.value) > 20:
            return self.value[:20] + "..."
        return self.value


class ProductProperty(models.Model):
    class Meta:
        verbose_name = "Свойство продукта"
        verbose_name_plural = "Свойства продукта"
        ordering = "name",

    name = models.ForeignKey(NameProductProperty, on_delete=models.PROTECT, blank=False, null=False)
    value = models.ForeignKey(ValueProductProperty, on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return f"{self.name}:{self.value}"


class ProductCategory(models.Model):
    name = models.CharField(max_length=50,)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    description = models.TextField(null=False, blank=True, verbose_name="Описание")
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="Цена")
    discount = models.PositiveSmallIntegerField(default=0, verbose_name="Скидка",
                                                validators=[MaxValueValidator(99,
                                                                              message="Значение не должно превышать %(limit_value)s")], )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Создатель", null=True)
    has_now = models.BooleanField(default=True, verbose_name="Наличие")
    archived = models.BooleanField(default=False, verbose_name="Архивный")
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Категория")
    properties = models.ManyToManyField(ProductProperty, related_name="products", verbose_name="Параметры")

    def __str__(self):
        str_ = f"Продукт {self.pk}"
        if not self.properties: return str_
        return str_ + f" ({'; '.join(str(property) for property in self.properties.all())})"


class Order(models.Model):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    delivery_address = models.TextField(null=False, blank=False, verbose_name="Адресс доставки")
    comment = models.CharField(max_length=200, null=True, blank=True, verbose_name="Комментарий")
    promocode = models.CharField(max_length=20, null=True, blank=True, verbose_name="Промокод")
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name="orders", verbose_name="Продукты")

    def __str__(self):
        return f"Заказ {self.pk}"

    @property
    def total_price(self):
        total = 0
        for product in self.products.all():
            total += float(product.price) - (float(product.price) * (float(product.discount) * 0.01))
        return total