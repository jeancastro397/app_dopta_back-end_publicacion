# from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from publicaciones.models import (
    Mascota,
    Evento,
    Informacion,
    Servicio
)
from .serializers import (
    EventoSerializer,
    InformacionSerializer,
    ServicioSerializer
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication








# class ListPubMascota(APIView):

#     def get(self, request):
#         try:
#             mascotas = Mascota.objects.all()
#             serializer = MascotaSerializer(mascotas, many=True)

#             if serializer.is_valid:
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             else:
#                 return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
#         except Mascota.DoesNotExist:
#             return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#         except Exception as e:
#             return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)



    # # Deshabilitar la renderización del formulario del filtro
    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['filtering'] = True
    #     return context


# class EventoViewSet(viewsets.ModelViewSet):
#     queryset = Evento.objects.all()
#     serializer_class = EventoSerializer


# class InformacionViewSet(viewsets.ModelViewSet):
#     queryset = Informacion.objects.all()
#     serializer_class = InformacionSerializer


# class ServicioViewSet(viewsets.ModelViewSet):
#     queryset = Servicio.objects.all()
#     serializer_class = ServicioSerializer

