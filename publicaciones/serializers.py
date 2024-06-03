from rest_framework import serializers
from publicaciones.models import Favorito


## Serializador para favoritos
class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = ['usuario', 'mascota', 'fecha_agregado']
        read_only_fields = ['usuario', 'fecha_agregado']
