from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'product', views.ProductListDetail)
router.register(r'product_auth', views.ProductListDetailDestroyAPIView)
urlpatterns = [
    path('', include(router.urls)),
    path('buy_product/', views.BuyProduct.as_view())
]
