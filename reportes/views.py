from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import (
    ReporteMascota,
    ReporteEvento,
    ReporteServicio
)
from .serializers import (
    ReporteMascotaSerializer,
    ReporteEventoSerializer,
    ReporteServicioSerializer
)
from publicaciones.models import (
    Mascota,
    Evento,
    Servicio
)
from rest_framework.serializers import Serializer
from itertools import chain


## CRUD DE REPORTES DE MASCOTA
# REPORTAR MASCOTA
class ReportarMascota(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            mascota = get_object_or_404(Mascota, pk=pk)
            reporte, created = ReporteMascota.objects.get_or_create(usuario=request.user, mascota=mascota)

            if created:
                return Response({"message": "Publicación de mascota reportada."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "La publicación ya se encuentra reportada por este usuario"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Remover la publicacion de los reportes (Tabla Reporte, no Mascota)
class RemoveReporteMascota(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        mascota = get_object_or_404(Mascota, pk=pk)
        reporte = get_object_or_404(ReporteMascota, usuario=request.user, mascota=mascota)
        reporte.delete()

        return Response({"message": "El reporte a sido revocado."}, status=status.HTTP_204_NO_CONTENT)



## CRUD DE REPORTES DE EVENTO
# REPORTAR EVENTO
class ReportarEvento(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            evento = get_object_or_404(Evento, pk=pk)
            reporte, created = ReporteEvento.objects.get_or_create(usuario=request.user, evento=evento)

            if created:
                return Response({"message": "Publicación de evento reportada."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "La publicación ya se encuentra reportada por este usuario"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Remover la publicacion de los reportes
class RemoveReporteEvento(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        reporte = get_object_or_404(ReporteEvento, usuario=request.user, evento=evento)
        reporte.delete()

        return Response({"message": "El reporte a sido revocado."}, status=status.HTTP_204_NO_CONTENT)



## CRUD DE REPORTES DE SERVICIOS
# REPORTAR SERVICIO
class ReportarServicio(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            servicio = get_object_or_404(Servicio, pk=pk)
            reporte, created = ReporteServicio.objects.get_or_create(usuario=request.user, servicio=servicio)

            if created:
                return Response({"message": "Publicación de servicio reportada."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "La publicación ya se encuentra reportada por este usuario"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Remover la publicacion de los reportes
class RemoveReporteServicio(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        reporte = get_object_or_404(ReporteServicio, usuario=request.user, servicio=servicio)
        reporte.delete()

        return Response({"message": "El reporte a sido revocado."}, status=status.HTTP_204_NO_CONTENT)



# Listar reportes del propio usuario
class ListReportesUsuario(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    # Combina los serializadores de las publicaciones
    def get_serializer_class(self):
        class CombinedSerializer(Serializer):
            reportes_mascota = ReporteMascotaSerializer(many=True)
            reportes_evento = ReporteEventoSerializer(many=True)
            reportes_sericio = ReporteServicioSerializer(many=True)

        return CombinedSerializer

    # Retorna la lista de reportes del usuario para cualquier publicacion reportada
    def get_queryset(self):
        reportes_mascota = ReporteMascota.objects.filter(usuario=self.request.user)
        reportes_evento = ReporteEvento.objects.filter(usuario=self.request.user)
        reportes_servicio = ReporteServicio.objects.filter(usuario=self.request.user)

        combined_querysets = list(chain(reportes_mascota, reportes_evento, reportes_servicio))
        
        return combined_querysets


# Listar reportes de todos los usuarios (solo admin)
class ListReportesAdmin(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
        'usuario__username': ['contains'],
        'motivo': ['contains'],
        'fecha_reporte': ['contains'],
        'estado': ['contains'],
    }

    def get_serializer_class(self):
        class CombinedSerializer(Serializer):
            reportes_mascota = ReporteMascotaSerializer(many=True)
            reportes_evento = ReporteEventoSerializer(many=True)
            reportes_servicio = ReporteServicioSerializer(many=True)

        return CombinedSerializer

    def get_queryset(self):
        reportes_mascota = ReporteMascota.objects.all()
        reportes_evento = ReporteEvento.objects.all()
        reportes_servicio = ReporteServicio.objects.all()

        combined_querysets = list(chain(reportes_mascota, reportes_evento, reportes_servicio))

        return combined_querysets
