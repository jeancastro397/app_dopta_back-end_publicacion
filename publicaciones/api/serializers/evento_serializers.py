from publicaciones.models import Evento
from favoritos.models import FavoritoEvento
from common.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer, DateTimeField, SerializerMethodField, ValidationError



class EventoSerializer(ModelSerializer):
    usuario = UserSerializer(read_only=True)
    is_favorito = SerializerMethodField()
    fec_public = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Evento
        fields = ['usuario', 'id', 'titulo', 'fec_public', 'descripcion', 'nombre', 'localizacion', 'fec_evento', 'is_favorito']
        read_only_fields = ['usuario']

    def create(self, validated_data):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            raise ValidationError("Usuario no autenticado")
        
        user = request.user
        evento = Evento.objects.create(usuario=user, **validated_data)
        evento.save()
        return evento


    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if not request or not request.user.is_authneticated:
            raise ValidationError("Usuario no autentificado")
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


    def get_is_favorito(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            return FavoritoEvento.objects.filter(usuario=request.user, evento=obj).exists()
        return False