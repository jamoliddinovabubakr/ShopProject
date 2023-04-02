from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_view),
    path('product/<int:pk>/', views.product_view),
    path('createproduct/', views.create_product),
    path('buyproduct/', views.buy_product),
    path('editproduct/', views.edit_product),
    path('deleteproduct/', views.delete_product)

]
