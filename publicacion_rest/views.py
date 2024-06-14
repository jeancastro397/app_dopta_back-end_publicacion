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
        endpoints_servicio = {
            "crear servicio (Token Auth)": "/servicios/crear-publicacion/",
            "listar servicios": "/servicios/lista-publicaciones/",
            "modificar servicio (Token Auth)": "/servicios/modificar-publicacion/<int:pk>",
            "eliminar servicio (Token Auth)": "/servicios/eliminar-publicacion/<int:pk>",
        }
        endpoints_favorito = {
            # Endpoints de Mascotas en Favoritos
            "agregar mascota favorito (Token Auth)": "/favoritos/agregar/mascota/<int:pk>",
            "remover mascota favorito (Token Auth)": "/favoritos/remover/mascota/<int:pk>",
            "listar mascotas favorito (Token Auth)": "/favoritos/listar/mascotas/",

            # Endpoints de Eventos en Favoritos
            "agregar evento favorito (Token Auth)": "/favoritos/agregar/evento/<int:pk>",
            "remover evento favorito (Token Auth)": "/favoritos/remover/evento/<int:pk>",
            "listar eventos favorito (Token Auth)": "/favoritos/listar/eventos/",

            # Endpoints de Servicios en Favoritos
            "agregar servicio favorito (Token Auth)": "/favoritos/agregar/servicio/<int:pk>",
            "remover servicio favorito (Token Auth)": "/favoritos/remover/servicio/<int:pk>",
            "listar servicios favorito (Token Auth)": "/favoritos/listar/servicios/",
        }
        endpoints_reporte = {
            # Endpoints de publicaciones de Mascota Reportadas
            "reportar publicacion mascota (Token Auth)": "/reportes/reportar-pub-mascota/<int:pk>",
            "remover reporte publicacion mascota (Token Auth)": "/reportes/remover-reporte-mascota/<int:pk>",

            # Endpoints de publicaciones de Evento Reportadas
            "reportar publicacion evento (Token Auth)": "/reportes/reportar-pub-evento/<int:pk>",
            "remover reporte publicacion evento (Token Auth)": "/reportes/remover-reporte-evento/<int:pk>",

            # Endpoints de publicaciones de Servicio Reportadas
            "reportar publicacion servicio (Token Auth)": "/reportes/reportar-pub-servicio/<int:pk>",
            "remover reporte publicacion servicio (Token Auth)": "/reportes/remover-reporte-servicio/<int:pk>",

            # Endpoints de listas de publicaciones Reportadas
            "listar reportes usuario (Token Auth)": "/reportes/listar-reportes-usuario/",
            "listar reportes admin (Token AdminUser)": "/reportes/listar-reportes-admin/"
        }
        endpoints = {
            "bienvenida": "/",
            "mascota": endpoints_mascota,
            "evento": endpoints_evento,
            "servicio": endpoints_servicio,
            "favorito": endpoints_favorito,
            "reporte": endpoints_reporte,
        }
        message = "¡Bienvenido a la API Publicaciones! Aquí están los endpoints disponibles:"
        return Response({"message": message, "endpoints": endpoints})