from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import VendorViewSet, PurchaseOrderViewSet

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
