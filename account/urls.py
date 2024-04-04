from django.urls import path
from .swagger import *

from account.views import login, logout, profile, registration

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-account'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-account'),
]

