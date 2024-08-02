from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from .models import Order, Product
from .forms import ProductForm, OrderForm

# Create your views here.

app_name = "shopapp"


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'shopapp/shop_index.html', context={
            "username": self.request.user.username
        })


class ProductsListView(ListView):
    model = Product
    template_name = 'shopapp/products_list.html'
    context_object_name = "products"
    queryset = Product.objects.prefetch_related("properties").filter(archived=False)


class ProductDetailView(DetailView):
    template_name = 'shopapp/product_detail.html'
    model = Product
    context_object_name = "product"


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "shopapp.add_product"
    model = Product
    template_name = "shopapp/create_product.html"
    fields = "category", "description", "price", "discount", "has_now", "archived", "properties"
    success_url = reverse_lazy("shopapp:products")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ProductCreateView, self).form_valid(form)


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):

        if self.request.user.is_superuser:
            return True
        author = self.get_object().created_by
        if self.request.user.has_perm("shopapp.change_product") and author == self.request.user:
            return True

    model = Product
    template_name = "shopapp/update_product.html"
    fields = "description", "price", "discount"

    def get_success_url(self):
        return reverse(
            "shopapp:product_detail", kwargs={
                "pk": self.object.pk
            }
        )


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrderListView(ListView):
    model = Order
    template_name = "shopapp/orders_list.html"
    context_object_name = "orders"
    queryset = Order.objects.select_related("user").prefetch_related("products").all()


class OrderCreateView(CreateView):
    model = Order
    template_name = "shopapp/create_order.html"
    context_object_name = "form"
    fields = "user", "delivery_address", "comment", "promocode", "products"
    success_url = reverse_lazy("shopapp:orders")


class OrderDetailView(DetailView):
    model = Order
    template_name = "shopapp/order_detail.html"
    context_object_name = "order"


class OrderUpdateView(UpdateView):
    model = Order
    template_name = "shopapp/update_order.html"
    fields = "user", "delivery_address", "comment", "promocode", "products"

    def get_success_url(self):
        return reverse(
            "shopapp:order_detail", kwargs={
                "pk": self.object.pk
            }
        )


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("shopapp:orders")
