from rest_framework import serializers
from publicaciones.api.mixins import FirebaseImageMixin
from publicaciones.models import Mascota, Favorito


class MascotaSerializer(FirebaseImageMixin, serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['usuario', 'titulo', 'fec_public', 'nom_mascota', 'especie', 'raza', 'sexo', 'tamanio', 'edad', 'foto', 'is_favorito']
        read_only_fields = ['usuario']


    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        # Crear la instancia de publicación sin la imagen aún
        mascota = Mascota.objects.create(usuario=user, **validated_data)

        # Si hay una imagen, subirla a Firebase
        foto = request.FILES.get('foto')
        if foto:
            public_url = self.upload_image_to_firebase(user, mascota.id, foto)
            mascota.foto = public_url
            mascota.save()

        return mascota

    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = request.user

        foto = request.FILES.get('foto')
        if foto:
            public_url = self.upload_image_to_firebase(user, instance.id, foto)
            instance.foto = public_url

        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.nom_mascota = validated_data.get('nom_mascota', instance.nom_mascota)
        instance.save()

        return instance

    # Funcion para inscribir campo favorito a publicacion mascota
    def get_is_favorito(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authemticated:
            return Favorito.objects.filter(usuario=request.user, mascota=obj).exists()
        return False