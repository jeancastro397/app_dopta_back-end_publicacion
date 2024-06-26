from django.urls import path
from publicaciones.api.views.mascota_views import (
    CreatePubMascota,
    ListPubMascota,
    ModificarPubMascota,
    DeletePubMascota
)


# URLS de vistas para Mascota
urlpatterns = [
    path('crear-publicacion/', CreatePubMascota.as_view(), name='create-pub-mascota'),
    path('lista-publicaciones/', ListPubMascota.as_view(), name='list-pub-mascota'),
    path('modificar-publicacion/<int:pk>', ModificarPubMascota.as_view(), name='modif-pub-mascota'),
    path('eliminar-publicacion/<int:pk>', DeletePubMascota.as_view(), name='eliminar-pub-mascota')
]