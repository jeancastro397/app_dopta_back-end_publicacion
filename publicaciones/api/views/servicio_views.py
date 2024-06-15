# Imports de Django
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
# Imports de rest_framework
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
# Imports de models y serialzers
from publicaciones.models import Servicio
from publicaciones.api.serializers.servicio_serializers import ServicioSerializer
from common.permissions import IsOrganizacion


## PUBLICACION DE SERVICIOS
# Crear publicaciones de Servicios 
class CreatePubServicio(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOrganizacion]

    def post(self, request, *args, **kwargs):

        try:
            serializer = ServicioSerializer(data=request.data, context={'request': request})

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Servicio guardado con éxito"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)


# Listar publicaciones de Servicios
class ListPubServicio(generics.ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
        'titulo': ['contains'],
        'fec_public': ['contains'],
        'tipo_servicio': ['contains'],
        'usuario__username': ['contains'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-fec_public')
        return Servicio.objects.all()


# Modificar publicacion de servicio
class ModificarPubServicio(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = {IsAuthenticated, IsOrganizacion}

    def patch(self, request, pk=None):
        try:
            servicio = get_object_or_404(Servicio, pk=pk)
            serializer = ServicioSerializer(servicio, data=request.data, partial=True, context={'request': request})

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except servicio.DoesNotExist:
            return Response({"message":"La publicación no existe"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Eliminar publicacion de Servicio
class DeletePubServicio(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOrganizacion]

    def delete(self, request, pk):
        try:
            servicio = Servicio.objects.get(pk=pk)
            servicio.delete()
            return Response({"message":"Publicación de servicio eliminada con éxito."})
        
        except Servicio.DoesNotExist:
            return Response({"message":"La publicación no existe"}, status=status.HTTP_404_NOT_FOUND)