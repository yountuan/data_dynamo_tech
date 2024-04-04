from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


account_schema_view = get_schema_view(
    openapi.Info(title='Accounts crm',
                 default_version='v1',
                 description='The account api documentation',
                 license=openapi.License(name='BSD license'),
                 ),
    public=True,
    permission_classes=[permissions.AllowAny,],

)