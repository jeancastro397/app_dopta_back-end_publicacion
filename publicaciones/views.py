from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from publicaciones.models import Mascota, Evento, Servicio
from common.permissions import IsAdministrador


# Para que el administrador pueda borrar cualquier publicacion
class DeletePublicacion(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdministrador]

    def delete(self, request, pk, tipo):
        model = None
        if tipo == 'mascota':
            model = Mascota
        elif tipo == 'evento':
            model = Evento
        elif tipo == 'servicio':
            model = Servicio

        if model:
            try:
                publicacion = get_object_or_404(model, pk=pk)
                publicacion.delete()
                return Response({"message": f"Publicación de {tipo} eliminada con éxito."}, status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Tipo de publicación no válido."}, status=status.HTTP_400_BAD_REQUEST)
