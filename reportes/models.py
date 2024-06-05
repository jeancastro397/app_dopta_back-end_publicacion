from django.conf import settings
from django.db import models


## Modelo para reportes de publicaciones
class Reporte(models.Model):
    MOTIVOS_REPORTE = [
        ('SPAM', 'Spam'),
        ('INAPROPIADO', 'Contenido inapropiado'),
        ('FRAUDE', 'Contenidoo fraudulento'),
        ('OTRO', 'Otro'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publicacion = models.ForeignKey('Publicacion', on_delete=models.CASCADE)
    motivo = models.CharField(choices=MOTIVOS_REPORTE, max_length=20)
    descripcion = models.TextField(null=False, blank=False)
    fecha_reporte = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Reportes"

    def __str__(self):
        return f"{self.usuario} reportó {self.publicacion} por {self.motivo}"