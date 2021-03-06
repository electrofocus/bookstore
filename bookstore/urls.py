from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from bookstore.docs import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui()),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh',
    ),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/', include('rest_framework.urls')),
    path('api/store/', include('store.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
