from django.urls import path
from .views import (
    AddFavoritoMascota,
    RemoveFavoritoMascota,
    ListFavoritosMascota,
    AddFavoritoEvento,
    RemoveFavoritoEvento,
    ListFavoritosEvento,
    AddFavoritoServicio,
    RemoveFavoritoServicio,
    ListFavoritosServicio
)


urlpatterns = [
    # Endpoints de Mascotas Favorito
    path('agregar/mascota/', AddFavoritoMascota.as_view(), name='add-mascota-favorito'),
    path('remover/mascota/<int:pk>', RemoveFavoritoMascota.as_view(), name='remove-mascota-favorito'),
    path('listar/mascotas/', ListFavoritosMascota.as_view(), name='list-mascota-favorito'),

    # Endpoints de Eventos favorito
    path('agregar/evento/', AddFavoritoEvento.as_view(), name='add-evento-favorito'),
    path('remover/evento/<int:pk>', RemoveFavoritoEvento.as_view(), name='remove-evento-favorito'),
    path('listar/eventos/', ListFavoritosEvento.as_view(), name='list-evento-favorito'),

    # Endpoints de Servicios Favorito
    path('agregar/servicio/', AddFavoritoServicio.as_view(), name='add-servicio-favorito'),
    path('remover/servicio/<int:pk>', RemoveFavoritoServicio.as_view(), name='remove-servicio-favorito'),
    path('listar/servicios/', ListFavoritosServicio.as_view(), name='list-servicio-favorito'),
]