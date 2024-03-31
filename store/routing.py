from django.urls import path

from . import consumers


websocket_urlpatterns = [
    path("ws/products/", consumers.ProductsConsumer.as_asgi()),
    path("ws/establishments/", consumers.EstablishmentsConsumer.as_asgi()),

]