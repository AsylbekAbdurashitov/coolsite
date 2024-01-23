from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from products.views import actor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("products.urls")),
    path('women/', include("women.urls")),
    path("products/", include("products.urls")),
    path('women/', include('women.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




