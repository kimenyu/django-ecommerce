from django.urls import path, include, re_path
from django.contrib import admin
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title="Django Ecommerce API")


# from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.social.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    path('products/', include('products.urls')),
    path('schema/', schema_view, name='openapi-schema'),
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]