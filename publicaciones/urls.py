from django.urls import path
from .views import (
    AddFavortio,
    RemoveFavorito,
    ListFavoritos
)


urlspatterns = [
    path('favorito/add/<int:pk>', AddFavortio.as_view(), name='add-favorito'),
    path('favorito/remove/<int:pk>', RemoveFavorito.as_view(), name='remove-favorito'),
    path('favoritos/', ListFavoritos.as_view(), name='list-favoritos'),
]