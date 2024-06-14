from django.contrib import admin
from django.urls import path, include
from publicaciones.api.urls.evento_urls import urlpatterns as eventos
from publicaciones.api.urls.mascota_urls import urlpatterns as mascotas
from publicaciones.api.urls.servicio_urls import urlpatterns as servicios
from reportes.urls import urlpatterns as reportes
from favoritos.urls import urlpatterns as favoritos
from .views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascotas/', include(mascotas)),
    path('eventos/', include(eventos)),
    path('servicios/', include(servicios)),
    path('reportes/', include(reportes)),
    path('favoritos/', include(favoritos)),
    path('', IndexView.as_view(), name='index'),
]
