from rest_framework import viewsets
from publicaciones.models import (
    Mascota,
    Evento,
    Informacion,
    Servicio
)
from .serializer import (
    MascotaSerializer,
    EventoSerializer,
    InformacionSerializer,
    ServicioSerializer
)


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class InformacionViewSet(viewsets.ModelViewSet):
    queryset = Informacion.objects.all()
    serializer_class = InformacionSerializer


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

