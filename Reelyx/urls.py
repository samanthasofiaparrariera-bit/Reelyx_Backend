
from django.http import HttpResponse
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings


admin.site.site_header = "Reelyx"
admin.site.index_title = "App Películas"

def home(request):
    return HttpResponse("""
    <html>
      <body style="background:#151315; color:white; font-family:Arial; text-align:center; padding:60px;">
        <h1>Reelyx API</h1>
        <p>Backend desplegado correctamente.</p>
        <a style="color:#bb81d9;" href="/api/peliculas/">Ver películas</a>
      </body>
    </html>
    """)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    path('api/users/', include('Users.urls')),
    path('api/peliculas/', include('Peliculas.urls')),
    path('api/listas/', include('Listas.urls')),
    path('api/reviews/', include('Reviews.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
