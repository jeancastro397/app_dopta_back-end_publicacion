from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from serializers.evento_serializers import EventoSerializer
from models import Evento
from django_filters.rest_framework import DjangoFilterBackend



## PUBLICACION DE EVENTOS
# Crear publicaciones eventos
class CreatePubEvento(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        try:
            serializer = EventoSerializer(data=request.data, context={'request':request})

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Evento guardado con éxito"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)


# Listar Eventos con fltros
class ListPubEvento(generics.ListAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
        'titulo': ['contains'],
        'fec_public': ['contains'],
        'fec_evento': ['contains'],
    }


# Modificar Evento
class ModificarPubEvento(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = {IsAuthenticated}

    def patch(self, request, pk=None):
        try:
            evento = get_object_or_404(Evento, pk=pk)
            
            serializer = EventoSerializer(evento, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Evento.DoesNotExist:
            return Response({"message":"La publicación no existe"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Eliminar Eventos
class DeletePubEvento(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            evento = Evento.objects.get(pk=pk)
            evento.delete()
            return Response({"message":"Publicación de evento eliminada con éxito."})
        
        except Evento.DoesNotExist:
            return Response({"message":"La publicación no existe"}, status=status.HTTP_404_NOT_FOUND)