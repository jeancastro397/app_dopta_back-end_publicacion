from rest_framework import serializers
from .models import Reporte
from django.contrib.contenttypes.models import ContentType



## Serializador para reportes
class ReporteSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField()

    class Meta:
        model = Reporte
        fields = ['usuario', 'content_type', 'motivo', 'descripcion', 'fecha_reporte']
        read_only_fields = ['usuario', 'fecha_reporte']

    def validate_content_type(self, value):
        try:
            ContentType.objects.get(model=value)
        except ContentType.DoesNotExist:
            raise serializers.ValidationError("Tipo de contenido no válido")
        return value