from django.urls import path, include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Bookstore API documentation",
      default_version='1.0',
      contact=openapi.Contact(email="amirmullagaliev@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   patterns=[
       path('api/store/', include('store.urls')),
   ]
)
