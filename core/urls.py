from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar

# SWAGGER
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    path('__debug__/', include(debug_toolbar.urls)),
]
