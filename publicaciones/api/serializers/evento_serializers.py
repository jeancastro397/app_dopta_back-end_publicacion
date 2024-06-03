from rest_framework.serializers import ModelSerializer
from publicaciones.models import Evento


class EventoSerializer(ModelSerializer):
    class Meta:
        model = Evento
        fields = ['usuario', 'titulo', 'fec_public', 'nombre', 'localizacion', 'fec_evento', 'descripcion']
        read_only_fields = ['usuario']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        evento = Evento.objects.create(usuario=user, **validated_data)
        return evento


    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = request.user

        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.save()

        return instance
