from rest_framework import serializers
from .models import Reporte


## Serializador para reportes
class ReporteSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = ['usuario', 'publicacion', 'motivo', 'descripcion', 'fecha_reporte']
        read_only_fields = ['usuario', 'fecha_reporte']