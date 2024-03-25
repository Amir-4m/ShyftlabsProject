from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Student Management API",
        default_version='v1',
        description="Student Management V1 APIs documentation."
    ),
    urlconf="shyftlabs.urls",
    public=True,

)
urlpatterns = [
    path('core/', include('apps.core.api.urls')),
    path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(
        r'^docs(?P<format>\.json)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),

]
