# from rest_framework.routers import DefaultRouter
# from .views import (
#     MascotaViewSet,
#     EventoViewSet,
#     InformacionViewSet,
#     ServicioViewSet
# )
from django.urls import path
from .views import (
    CreatePubMascota,
    ListPubMascota,
    ModificarPubMascota,
    DeletePubMascota,
)

urlpatterns = [
    path('create-mascotas/', CreatePubMascota.as_view(), name='create-mascotas'),
    path('list-mascotas/', ListPubMascota.as_view(), name='list-mascotas'),
    path('modificar-mascota/<int:pk>', ModificarPubMascota.as_view(), name='modificar-mascota'),
    path('eliminar-mascota/<int:pk>', DeletePubMascota.as_view(), name='eliminar-mascota'),
]



# router = DefaultRouter()
# router.register('mascotas', MascotaViewSet, basename='mascota')
# router.register('eventos', EventoViewSet, basename='evento')
# router.register('informaciones', InformacionViewSet, basename='informacion')
# router.register('servicios', ServicioViewSet, basename='servicio')

# urlpatterns = router.urls