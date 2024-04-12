from django.urls import path
from .swagger import account_schema_view
from django.conf import settings
from django.conf.urls.static import static


from account.views import login, logout, profile, registration

app_name='account'
urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('swagger/', account_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-account'),
    path('redoc/', account_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-account'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)