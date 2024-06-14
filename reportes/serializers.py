from .models import ReporteMascota, ReporteEvento, ReporteServicio
from rest_framework.serializers import ModelSerializer, DateTimeField
from publicaciones.api.serializers.mascota_serializers import MascotaSerializer
from publicaciones.api.serializers.evento_serializers import EventoSerializer
from publicaciones.api.serializers.servicio_serializers import ServicioSerializer
from common.serializers import UserSerializer



## Serializador para reportes de publicaciones de Mascota
class ReporteMascotaSerializer(ModelSerializer):
    usuario = UserSerializer(read_only=True)
    mascota = MascotaSerializer(read_only=True)
    fecha_reporte = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = ReporteMascota
        fields = ['usuario', 'mascota', 'motivo', 'descripcion', 'fecha_reporte']
        read_only_fields = ['usuario', 'fecha_reporte']



## Serializador para reportes de publicaciones de Evento
class ReporteEventoSerializer(ModelSerializer):
    usuario = UserSerializer(read_only=True)
    evento = EventoSerializer(read_only=True)
    fecha_reporte = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = ReporteEvento
        fields = ['usuario', 'evento', 'motivo', 'descripcion', 'fecha_reporte']
        read_only_fields = ['usuario', 'fecha_reporte']



## Serializador para reportes de publicaciones de Evento
class ReporteServicioSerializer(ModelSerializer):
    usuario = UserSerializer(read_only=True)
    servicio = ServicioSerializer(read_only=True)
    fecha_reporte = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = ReporteServicio
        fields = ['usuario', 'servicio', 'motivo', 'descripcion', 'fecha_reporte']
        read_only_fields = ['usuario', 'fecha_reporte']