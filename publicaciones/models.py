from django.conf import settings
from django.db import models
from django.utils import timezone



# Models Abstract Publicacion
class Publicacion(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    fec_public = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=255, null=False, blank=False)

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.titulo


# Models Mascota
class Mascota(Publicacion):
    list_sexo = [
    ('M' , 'Macho'),
    ('H' , 'Hembra'),
]
    nom_mascota = models.CharField(max_length=100, null=False, blank=False)
    especie = models.CharField(max_length=50, null=False, blank=False)
    raza = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(choices=list_sexo, max_length=20, null=False)
    tamanio = models.CharField(max_length=50, null=False, blank=False)
    edad = models.CharField(max_length=50, null=False, blank= False)
    foto = models.URLField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.nom_mascota


# Models Evento
class Evento(Publicacion):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    localizacion = models.CharField(max_length=255, null=False, blank=False)
    fec_evento = models.DateField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.nombre


# Models Servicio
class Servicio(Publicacion):
    tipo_servicio = models.CharField(max_length=50, null=False, blank=False)
    ubicacion = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.pk
