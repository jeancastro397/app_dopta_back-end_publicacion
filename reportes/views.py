from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status, generics
from publicaciones.models import Mascota
from .models import Reporte
from .serializers import ReporteSerializer
from django.contrib.contenttypes.models import ContentType


### CRUD DE REPORTES
# Agregar un reporte (reportar una publicacion)
class Reportar(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        serializer = ReporteSerializer(data=request.data)
        if serializer.is_valid():
            content_type = serializer.validated_data.get('content_type')
            content_type = ContentType.objects.get(model=content_type)
            model_class = content_type.model_class()
            content_object = get_object_or_404(model_class, pk=pk)

            Reporte.objects.create(
                usuario=request.user,
                content_object=content_object,
                motivo=serializer.validated_data.get('motivo'),
                descripcion=serializer.validated_data.get('descripcion')
            )
            return Response({"message": "Publicación reportada con éxito"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Listar reportes mandados, sólo un  usuario administrador puede listarlos
class Reportes(generics.ListAPIView):
    permission_classes = [IsAdminUser]

    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
