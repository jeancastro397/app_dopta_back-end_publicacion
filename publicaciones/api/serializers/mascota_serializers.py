from rest_framework import serializers
from publicaciones.api.mixins import FirebaseImageMixin
from publicaciones.models import Mascota
from favoritos.models import FavoritoMascota
from common.serializers import UserSerializer



class MascotaSerializer(FirebaseImageMixin, serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    is_favorito = serializers.SerializerMethodField()
    foto_archivo = serializers.ImageField(write_only=True, required=False)

    fec_public = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Mascota
        fields = ['usuario', 'id', 'titulo', 'fec_public', 'nom_mascota', 'especie', 'raza', 'sexo', 'tamanio', 'edad', 'foto', 'descripcion', 'is_favorito', 'foto_archivo']
        read_only_fields = ['usuario']

    def create(self, validated_data):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError("Usuario no autenticado")

        user = request.user

        # Extraer el archivo de imagen de los datos validados
        foto = validated_data.pop('foto_archivo', None)
        print(f"Foto archivo: {foto}")

        # Crear la instancia de publicación sin la imagen aún
        mascota = Mascota.objects.create(usuario=user, **validated_data)

        # Si hay una imagen, subirla a Firebase
        if foto:
            public_url = self.upload_image_to_firebase(mascota, foto)
            if public_url:
                mascota.foto = public_url
                mascota.save()
                print(f"Imagen subida con URL: {public_url}")
            else:
                print("Error subiendo la imagen a Firebase")

        return mascota

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError("Usuario no autenticado")

        foto = validated_data.pop('foto_archivo', None)
        if foto:
            public_url = self.upload_image_to_firebase(instance, foto)
            if public_url:
                instance.foto = public_url

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

    def get_is_favorito(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            return FavoritoMascota.objects.filter(usuario=request.user, mascota=obj).exists()
        return False

    def delete(self, instance):
        # Eliminar la imagen de Firebase si existe
        self.delete_image_from_firebase(instance)
        # Eliminar la instancia
        instance.delete()
