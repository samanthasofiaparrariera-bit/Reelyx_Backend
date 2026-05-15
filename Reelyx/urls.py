

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings


admin.site.site_header = "Reelyx"
admin.site.index_title = "App Películas"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/users/', include('Users.urls')),
    path('api/peliculas/', include('Peliculas.urls')),
    path('api/listas/', include('Listas.urls')),
    path('api/reviews/', include('Reviews.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
