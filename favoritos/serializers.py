from .models import FavoritoMascota, FavoritoEvento, FavoritoServicio
from rest_framework.serializers import ModelSerializer, DateTimeField
from publicaciones.api.serializers.mascota_serializers import MascotaSerializer
from publicaciones.api.serializers.evento_serializers import EventoSerializer
from publicaciones.api.serializers.servicio_serializers import ServicioSerializer
from common.serializers import UserSerializer


# Serializador para el modelo de Mascota Favorito
class FavoritoMascotaSerializer(ModelSerializer):
    usuario = UserSerializer(read_only=True)
    mascota = MascotaSerializer(read_only=True)
    fecha_agregado = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    
    class Meta:
        model = FavoritoMascota
        fields = ['usuario', 'mascota', 'fecha_agregado']
        read_only_fields = ['usuario', 'fecha_agregado']


# Serializadorpara el modelo de Evento Favorito
class FavoritoEventoSerializer(ModelSerializer):
    usuario = UserSerializer(read_only=True)
    evento = EventoSerializer(read_only=True)
    fecha_agregado = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = FavoritoEvento
        fields = ['usuario', 'evento', 'fecha_agregado']
        read_only_fields = ['usuario', 'fecha_agregado']


# serializador para el modelo de Servicio Favorito
class FavoritoServicioSerializer(ModelSerializer):
    usuario = UserSerializer(read_only=True)
    servicio = ServicioSerializer(read_only=True)
    fecha_agregado = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    
    class Meta:
        model = FavoritoServicio
        fields = ['usuario', 'servicio', 'fecha_agregado']
        read_only_fields = ['usuario', 'fecha_agregado']
