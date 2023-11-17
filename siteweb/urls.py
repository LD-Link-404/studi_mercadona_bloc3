from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from store.views import catalog, product_detail, search
from siteweb import settings
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog, name='catalog'),
    path('search/', search, name='search'),
    path('product/<str:slug>', product_detail, name="product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)