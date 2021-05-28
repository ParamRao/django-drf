from django.urls import path

from api import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Assignment API')

urlpatterns = [
    path('', views.home, name='Sample Assignment APIs'),
    path('ping/', views.ping_view, name='ping API'),
    path('info/', views.info_view, name='info API'),
    path('swagger-api/', schema_view, name='Swagger API'),
]
