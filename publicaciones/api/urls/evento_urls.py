from django.urls import path
from publicaciones.api.views.evento_views import (
    CreatePubEvento,
    ListPubEvento,
    ModificarPubEvento,
    DeletePubEvento
)


# URLS de vistas para Evento
urlpatterns = [
    path('crear-publicacion/', CreatePubEvento.as_view(), name='create-pub-evento'),
    path('lista-publicaciones/', ListPubEvento.as_view(), name='list-pub-evento'),
    path('modificar-publicacion/<int:pk>', ModificarPubEvento.as_view(), name='modif-pub-evento'),
    path('eliminar-publicacion/', DeletePubEvento.as_view(), name='eliminar-pub-evento')
]
