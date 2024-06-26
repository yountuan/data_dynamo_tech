from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

store_schema_view = get_schema_view(
    openapi.Info(title='Products inventory',
                 default_version='v1',
                 description='The products inventory api documentation',
                 license=openapi.License(name='BSD license'),
                 ),
    public=True,
    permission_classes=[permissions.AllowAny,],

)