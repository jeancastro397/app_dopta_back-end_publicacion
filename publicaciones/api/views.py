# from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from publicaciones.models import (
    Mascota,
    Evento,
    Informacion,
    Servicio
)
from .serializers import (
    MascotaSerializer,
    EventoSerializer,
    InformacionSerializer,
    ServicioSerializer
)


## PUBLICACION MASCOTA 
# Crear publicaciones mascota
class CreatePubMascota(APIView):

    def post(self, request):
        try:
            serializer = MascotaSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                return Response({"message":"Mascota guardada con exito"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Listar Mascotas
class ListPubMascota(APIView):

    def get(self, request):
        try:
            mascotas = Mascota.objects.all()
            serializer = MascotaSerializer(mascotas)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Mascota.DoesNotExist:
            return Response({"message":"No se encontraron publicaciones de mascotas."}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_404_NOT_FOUND)


# Modificar Mascota
class ModificarPubMascota(APIView):

    def patch(self, request, pk=None):
        try:
            mascota = get_object_or_404(Mascota, pk=pk)
            
            serializer = MascotaSerializer(mascota, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Mascota.DoesNotExist:
            return Response({"message":"La publicación no existe"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Eliminar Mascotas
class DeletePubMascota(APIView):

    def delete(self, pk):
        try:
            mascota = Mascota.objects.get(pk=pk)
            mascota.delete()
            return Response({"message":"Publicación de mascota eliminada con éxito."})
        
        except Mascota.DoesNotExist:
            return Response({"message":"La publicación no existe"}, status=status.HTTP_404_NOT_FOUND)


# class MascotaViewSet(viewsets.ModelViewSet):
#     queryset = Mascota.objects.all()
#     serializer_class = MascotaSerializer


# class EventoViewSet(viewsets.ModelViewSet):
#     queryset = Evento.objects.all()
#     serializer_class = EventoSerializer


# class InformacionViewSet(viewsets.ModelViewSet):
#     queryset = Informacion.objects.all()
#     serializer_class = InformacionSerializer


# class ServicioViewSet(viewsets.ModelViewSet):
#     queryset = Servicio.objects.all()
#     serializer_class = ServicioSerializer

