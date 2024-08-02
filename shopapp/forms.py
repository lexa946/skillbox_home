from django import forms

from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "category", "price", "discount", "properties","has_now", "archived"



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "user", "delivery_address", "comment", "promocode", "products"