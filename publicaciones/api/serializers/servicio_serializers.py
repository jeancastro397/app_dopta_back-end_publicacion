from rest_framework.serializers import SerializerMethodField, ModelSerializer, DateTimeField, ValidationError
from publicaciones.models import Servicio
from favoritos.models import FavoritoServicio
from common.serializers import UserSerializer



class ServicioSerializer(ModelSerializer):
    usuario = UserSerializer(read_only=True)
    fec_public = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    is_favorito = SerializerMethodField()

    class Meta:
        model = Servicio
        fields = ['usuario', 'id', 'titulo', 'fec_public', 'descripcion', 'tipo_servicio', 'ubicacion', 'is_favorito']
        read_only_fields = ['usuario']


    def create(self, validated_data):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            raise ValidationError("Usuario no autentificado")

        servicio = Servicio.objects.create(usuario = request.user, **validated_data)
        servicio.save()

        return servicio


    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if not request or not request.user.is_authenticated:
            raise ValidationError("Usuario no autentificado")
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


    def get_is_favorito(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            return FavoritoServicio.objects.filter(usuario=request.user, Servicio=obj).exists()

        return False
