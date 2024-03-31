from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, LocationViewSet, EstablishmentViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'establishments', EstablishmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]