from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .models import (
    FavoritoMascota,
    FavoritoEvento,
    FavoritoServicio
)
from .serializers import (
    FavoritoMascotaSerializer, 
    FavoritoEventoSerializer, 
    FavoritoServicioSerializer
)
from publicaciones.models import (
    Mascota,
    Evento,
    Servicio,
)
from common.permissions import IsPersonaOrOrganizacion, IsOrganizacion


## CRUD DE FAVORITOS MASCOTA
# Agregar Mascota a Favorito
class AddFavoritoMascota(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsPersonaOrOrganizacion]

    def post(self, request, pk):
        try:
            mascota = get_object_or_404(Mascota, pk=pk)
            favorito, created = FavoritoMascota.objects.get_or_create(usuario=request.user, mascota=mascota)

            if created:
                return Response({"message": "Mascota añadida a favoritos"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "La mascota ya se encuentra en favoritos"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Remover la mascota de favoritos
class RemoveFavoritoMascota(APIView):
    permission_classes = [IsAuthenticated, IsPersonaOrOrganizacion]

    def delete(self, request, pk):
        mascota = get_object_or_404(Mascota, pk=pk)
        favorito = get_object_or_404(FavoritoMascota, usuario=request.user, mascota=mascota)
        favorito.delete()

        return Response({"message": "Mascota eliminada de favoritos"}, status=status.HTTP_204_NO_CONTENT)


# Listar mascotas en favoritos
class ListFavoritosMascota(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsPersonaOrOrganizacion]
    serializer_class = FavoritoMascotaSerializer

    def get_queryset(self):
        return FavoritoMascota.objects.filter(usuario=self.request.user)



## CRUD DE FAVORITOS EVENTO
# Agregar Evento a Favorito
class AddFavoritoEvento(APIView):
    permission_classes = [IsAuthenticated, IsPersonaOrOrganizacion]

    def post(self, request, pk):
        try:
            evento = get_object_or_404(Evento, pk=pk)
            favorito, created = FavoritoEvento.objects.get_or_create(usuario=request.user, evento=evento)

            if created:
                return Response({"message": "Evento añadido a favoritos"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "El evento ya se encuentra en favoritos"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Remover el evento de favoritos
class RemoveFavoritoEvento(APIView):
    permission_classes = [IsAuthenticated, IsPersonaOrOrganizacion]

    def delete(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        favorito = get_object_or_404(FavoritoEvento, usuario=request.user, evento=evento)
        favorito.delete()

        return Response({"message": "Evento eliminado de favoritos"}, status=status.HTTP_204_NO_CONTENT)


# Listar eventos en favoritos
class ListFavoritosEvento(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsPersonaOrOrganizacion]
    serializer_class = FavoritoEventoSerializer

    def get_queryset(self):
        return FavoritoEvento.objects.filter(usuario=self.request.user)



## CRUD DE FAVORITOS SERVICIO
# Agregar servicio a favoritos
class AddFavoritoServicio(APIView):
    permission_classes = [IsAuthenticated, IsPersonaOrOrganizacion]

    def post(self, request, pk):
        try:
            servicio = get_object_or_404(Servicio, pk=pk)
            favorito, created = FavoritoServicio.objects.get_or_create(usuario=request.user, servicio=servicio)

            if created:
                return Response({"message": "Servicio añadido a favoritos"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "El servicio ya se encuentra en favoritos"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Remover servicio de favoritos
class RemoveFavoritoServicio(APIView):
    permission_classes = [IsAuthenticated, IsPersonaOrOrganizacion]

    def delete(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        favorito = get_object_or_404(FavoritoServicio, usuario=request.user, servicio=servicio)
        favorito.delete()

        return Response({"message": "Servicio eliminado de favoritos"}, status=status.HTTP_204_NO_CONTENT)


# Listar servicios en favoritos
class ListFavoritosServicio(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsPersonaOrOrganizacion]
    serrializer = FavoritoServicioSerializer

    def get_queryset(self):
        return FavoritoServicio.objects.filter(usuario=self.request.user)