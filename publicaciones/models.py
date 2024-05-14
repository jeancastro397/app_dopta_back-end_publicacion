from django.db import models
from django.utils import timezone

list_sexo = [
    ('M' , 'Macho'),
    ('H' , 'Hembra'),
]

class Publicacion(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    fec_public = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.titulo


class Mascota(Publicacion):
    nom_mascota = models.CharField(max_length=100, null=False, blank=False)
    especie = models.CharField(max_length=50, null=False, blank=False)
    raza = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(choices=list_sexo, max_length=20, null=False)
    tamanio = models.CharField(max_length=50, null=False, blank=False)
    edad = models.CharField(max_length=50, null=False, blank= False)
    foto = models.ImageField(upload_to='mascotas/' , null=True, blank=True)

    def __str__(self):
        return self.nom_mascota


class Evento(Publicacion):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    localizacion = models.CharField(max_length=255, null=False, blank=False)
    fec_evento = models.DateField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.nombre


class Servicio(Publicacion):
    tipo_servicio = models.CharField(max_length=50, null=False, blank=False)
    ubicacion = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.pk
    

class Informacion(Publicacion):
    subtitulo = models.CharField(max_length=100, null=False, blank=False)
    contenido = models.TextField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.pk