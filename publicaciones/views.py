from django.shortcuts import get_object_or_404
from publicaciones.models import Favorito, Mascota
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from publicaciones.api.serializers.mascota_serializers import MascotaSerializer
from .serializers import FavoritoSerializer



### CRUD DE FAVORITOS
## Agregar publicacion a favoritos
class AddFavorito(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        mascota = get_object_or_404(Mascota, pk=pk)
        favorito, created = Favorito.objects.get_or_create(usuario=request.user, mascota=mascota)
        if created:
            return Response({"message": "Mascota añadida a favoritos"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Mascota ya está en favoritos"}, status=status.HTTP_200_OK)



## Eliminar publicacion de favoritos
class RemoveFavorito(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        mascota = get_object_or_404(Mascota, pk=pk)
        favorito = get_object_or_404(Favorito, usuario=request.user, mascota=mascota)
        favorito.delete()
        
        return Response({'message': 'Mascota eliminada de favoritos'}, status=status.HTTP_204_NO_CONTENT)


## Listar publicaciones de favoritos
class ListFavoritos(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favoritos = Favorito.objects.filter(usuario=request.user).select_related('mascota')
        mascotas = [favorito.mascota for favorito in favoritos]
        serializer = MascotaSerializer(mascotas, many=True, context={'request': request})
        return Response(serializer.data)
