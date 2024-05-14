from rest_framework import serializers
from publicaciones.models import (
    Mascota,
    Evento,
    Informacion,
    Servicio
)


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class InformacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informacion
        fields = '__all__'


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

