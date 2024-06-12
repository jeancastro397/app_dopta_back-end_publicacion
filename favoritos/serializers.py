from rest_framework.serializers import ModelSerializer, DateTimeField
from .models import FavoritoMascota, FavoritoEvento, FavoritoServicio


# Serializador para el modelo de Mascota Favorito
class FavoritoMascotaSerializer(ModelSerializer):
    fecha_agregado = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    
    class Meta:
        model = FavoritoMascota
        fields = ['usuario', 'mascota', 'fecha_agregado']
        read_only_fields = ['usuario', 'fecha_agregado']


# Serializadorpara el modelo de Evento Favorito
class FavoritoEventoSerializer(ModelSerializer):
    fecha_agregado = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = FavoritoEvento
        fields = ['usuario', 'evento', 'fecha_agregado']
        read_only_fields = ['usuario', 'fecha_agregado']


# serializador para el modelo de Servicio Favorito
class FavoritoServicioSerializer(ModelSerializer):
    fecha_agregado = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    
    class Meta:
        model = FavoritoServicio
        fields = ['usuario', 'servicio', 'fecha_agregado']
        read_only_fields = ['usuario', 'fecha_agregado']
