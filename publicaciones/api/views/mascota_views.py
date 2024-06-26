from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from publicaciones.models import Mascota
from publicaciones.api.serializers.mascota_serializers import MascotaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from common.permissions import IsPersonaOrOrganizacion


## PUBLICACION MASCOTA 
# Crear publicaciones mascota
class CreatePubMascota(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsPersonaOrOrganizacion]

    def post(self, request, *args, **kwargs):

        try:
            serializer = MascotaSerializer(data=request.data, context={'request':request})

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Mascota guardada con éxito"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)



# Listar Mascotas con filtros
class ListPubMascota(generics.ListAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    filter_backends = [DjangoFilterBackend]
    
    # Agrega el campo del usuario a los filtros
    filterset_fields = {
        'titulo': ['contains'],
        'especie': ['contains'],
        'raza': ['contains'],
        'sexo': ['contains'],
        'usuario__username': ['contains']  # Filtro para el nombre de usuario
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-fec_public')
        return Mascota.objects.all()


# Modificar Mascota
class ModificarPubMascota(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsPersonaOrOrganizacion]

    def patch(self, request, pk=None):
        try:
            mascota = get_object_or_404(Mascota, pk=pk)
            serializer = MascotaSerializer(mascota, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Mascota.DoesNotExist:
            return Response({"message": "La publicación no existe"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Eliminar Mascotas
class DeletePubMascota(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsPersonaOrOrganizacion]

    def delete(self, request, pk):
        try:
            mascota = Mascota.objects.get(pk=pk)
            mascota.delete()
            return Response({"message":"Publicación de mascota eliminada con éxito."})
        
        except Mascota.DoesNotExist:
            return Response({"message":"La publicación no existe"}, status=status.HTTP_404_NOT_FOUND)