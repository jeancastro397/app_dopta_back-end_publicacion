from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class IndexView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        endpoints_mascota = {
            "crear mascota (Token Auth)": "/mascotas/crear-publicacion/",
            "listar mascotas": "/mascotas/lista-publicaciones/",
            "modificar mascota (Token Auth)": "/mascotas/modificar-publicacion/<int:pk>",
            "eliminar mascota (Token Auth)": "/mascotas/eliminar-publicacion/<int:pk>",
        }
        endpoints_evento = {
            "crear evento (Token Auth)": "/eventos/crear-publicacion/",
            "listar eventos": "/eventos/lista-publicaciones/",
            "modificar evento (Token Auth)": "/eventos/modificar-publicacion/<int:pk>",
            "eliminar evento (Token Auth)": "/eventos/eliminar-publicacion/<int:pk>",
        }
        endpoints = {
            "bienvenida": "/",
            "mascota": endpoints_mascota,
            "evento": endpoints_evento,
        }
        message = "¡Bienvenido a la API Publicaciones! Aquí están los endpoints disponibles:"
        return Response({"message": message, "endpoints": endpoints})