from django.urls import path, include

from .views import IndexView, ProductsListView, ProductDetailView, ProductCreateView, ProductUpdateView,\
    ProductDeleteView, OrderListView, OrderCreateView, OrderDetailView, OrderUpdateView, OrderDeleteView
app_name = "shopapp"


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='create_product'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='update_product'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='delete_product'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('orders/create/', OrderCreateView.as_view(), name='create_order'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/update', OrderUpdateView.as_view(), name='update_order'),
    path('orders/<int:pk>/delete', OrderDeleteView.as_view(), name='delete_order'),

]
