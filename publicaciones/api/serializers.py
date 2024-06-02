from rest_framework import serializers
from publicaciones.api.mixins import FirebaseImageMixin
from publicaciones.models import (
    Mascota,
    Evento,
    Informacion,
    Servicio
)





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

