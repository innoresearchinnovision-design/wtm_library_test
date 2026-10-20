"""
URL configuration for library_ms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
# schema_view  =  get_schema_view(
#     openapi.Info(
#         title="Yeukai Library API",
#         default_version="vAgnes",
#         description="Library OpenAPI for testing",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="liuyuenfu@gmail.com"),
#         license=openapi.License(name="Not so Free License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,)
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home_app.urls")),
    path("accounts/", include("accounts.urls")),
    path("author/", include("author.urls")),
    path("book/", include("book_app.urls")),
    path("genre/", include("genre_app.urls")),
    #YASG
    # path("swagger<format>/",schema_view.without_ui(cache_timeout=0),name="schema_json"),
    # path("swagger/",schema_view.with_ui("swagger",cache_timeout=0),name="schema-swagger-ui"),
    # path("redoc",schema_view.with_ui("redoc",cache_timeout=0),name="schema-redoc")
    #drf spectular
    path("api/schema/",SpectacularAPIView.as_view(),name="schema"),
    path("swagger/",SpectacularSwaggerView.as_view(url_name='schema'),name="swagger-ui"),
    path("redoc/",SpectacularRedocView.as_view(url_name='schema'),name="redoc"),

    #JWT TOKEN
    path("api-token/",TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path("api-refresh-token/",TokenRefreshView.as_view(),name="token_refresh"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + debug_toolbar_urls()
