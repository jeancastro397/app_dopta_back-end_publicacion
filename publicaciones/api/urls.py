from rest_framework.routers import DefaultRouter
from .views import (
    MascotaViewSet,
    EventoViewSet,
    InformacionViewSet,
    ServicioViewSet
)


router = DefaultRouter()
router.register('mascotas', MascotaViewSet, basename='mascota')
router.register('eventos', EventoViewSet, basename='evento')
router.register('informaciones', InformacionViewSet, basename='informacion')
router.register('servicios', ServicioViewSet, basename='servicio')

urlpatterns = router.urls