from django.urls import path
from publicaciones.api.views.servicio_views import (
    CreatePubServicio,
    ListPubServicio,
    ModificarPubServicio,
    DeletePubServicio
)


# URLS de vistas para Servicio
urlpatterns = [
    path('crear-publicacion/', CreatePubServicio.as_view(), name='create-pub-servicio'),
    path('lista-publicaciones/', ListPubServicio.as_view(), name='list-pub-servicio'),
    path('modificar-publicacion/<int:pk>', ModificarPubServicio.as_view(), name='modif-pub-servicio'),
    path('eliminar-publicacion/<int:pk>', DeletePubServicio.as_view(), name='eliminar-pub-servicio')
]