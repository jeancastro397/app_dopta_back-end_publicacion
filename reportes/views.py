from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from publicaciones.models import Publicacion
from .models import Reporte
from rest_framework.response import Response
from rest_framework import status



### CRUD DE REPORTES
# Agregar un reporte (reportar una publicacion)
class Reportar(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        publicacion = get_object_or_404(Publicacion, pk=pk)
        reporte, created = Reporte.objects.get_or_create(usuario=request.user, publicacion=publicacion)
        if created:
            return Response({"message": "Publicación reportada con éxito"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "La publicación ya se encuentra en revisión"}, status=status.HTTP_200_OK)