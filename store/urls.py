from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, LocationViewSet, EstablishmentViewSet, CategoryViewSet
from .swagger import store_schema_view
from rest_framework.authtoken import views
from . import views
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'establishments', EstablishmentViewSet)

#url paths
urlpatterns = [
    path('', include(router.urls)),
    path('lobby/products/', views.lobby, name='products'),
    path('lobby/establishments/', views.lobby_e, name='establishments'),
    path('swagger/', store_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-store'),
    path('redoc/', store_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-store'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)