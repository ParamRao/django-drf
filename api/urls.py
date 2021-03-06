from django.urls import path

from api import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Assignment API",
        default_version='v1',
        description="Sample Assignment APIs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="parameshwar.rao@outlook.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('ping/', views.ping_view, name='Ping API'),
    path('list-ping/', views.list_ping_view, name='List of Ping Made'),
    path('info/', views.info_view, name='Info API'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
