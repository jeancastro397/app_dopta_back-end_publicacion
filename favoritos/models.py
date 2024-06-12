from django.db import models
from django.conf import settings
from publicaciones.models import Mascota, Evento, Servicio



## Modelo para guardar publicaciones de mascota como favorito
# Relación ForeignKey hacia Mascota
class FavoritoMascota(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'mascota')
        verbose_name_plural = 'Favoritos Mascota'

    def __str__(self):
        return f"{self.usuario} - {self.mascota}"


# Modelo con relación a publicaciones de Evento
class FavoritoEvento(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'evento')
        verbose_name_plural = 'Favoritos Evento'
    
    def __str__(self):
        return f"{self.usuario} - {self.evento}"


# Modelo con relación a publicaciones de Servicio
class FavoritoServicio(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'servicio')
        verbose_name_plural = 'Favoritos Servicio'
    
    def __str__(self):
        return f"{self.usuario} - {self.servicio}"

