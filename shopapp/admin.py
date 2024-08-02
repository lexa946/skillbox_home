from django.contrib import admin
from .models import Product, Order, ProductProperty, ValueProductProperty, NameProductProperty, ProductCategory

from .admin_other.admin_action import mark_archived, mark_unarchived, mark_has_now, mark_no_has_now
from .admin_other.admin_mixins import ExportAsCSVMixin



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(NameProductProperty)
class NameProductPropertyAdmin(admin.ModelAdmin):
    pass

@admin.register(ValueProductProperty)
class ValueProductPropertyAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    pass

class OrderInline(admin.TabularInline):
    model = Product.orders.through
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [mark_archived, mark_unarchived, mark_has_now, mark_no_has_now, "export_csv"]
    list_display = "pk", "name_product", "category", "price", "discount", "created_at_russian", "updated_at_russian", "has_now",  "archived"
    list_display_links = "pk", "name_product",
    search_fields = "pk", "category__name",
    ordering = "category",

    inlines = [
        OrderInline,
    ]

    fieldsets = [
        (None, {
            "fields": ("description", "category", "properties", "created_by"),
            "classes": ("wide",),
        }),

        ("Настройки цены", {
            "fields": ("price", "discount"),
            "classes": ("wide",),
        }),

        ("Дополнительные опции", {
            "fields": ("has_now", "archived"),
            "classes": ("wide", "collapse"),
        }),
    ]


    def name_product(self, obj: Product):
        if obj.category is None: return ""
        properties = obj.properties.all()
        try:
            match obj.category.name:
                case "Пластик":
                    color = properties.get(name__name="Цвет").value
                    type_ = properties.get(name__name="Тип пластика").value
                    return f'{type_} пластик "{color}"'
                case "Принтер":
                    return properties.get(name__name="Название").value
        except ProductProperty.MultipleObjectsReturned:
            return "Не валидное значение параметров"
        return ""
    name_product.short_description = "Название"

    def created_at_russian(self, obj: Product):
        return obj.created_at.strftime("%d.%m.%Y %H:%M")
    created_at_russian.short_description = "Дата создания"


    def updated_at_russian(self, obj: Product):
        return obj.updated_at.strftime("%d.%m.%Y %H:%M")
    updated_at_russian.short_description = "Дата изменения"

    def get_queryset(self, request):
        return Product.objects.prefetch_related("properties")



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = "user_verbose", "delivery_address", "comment", "promocode", "created_at"


    def user_verbose(self, obj: Order) ->str:
        return obj.user.first_name or obj.user.username