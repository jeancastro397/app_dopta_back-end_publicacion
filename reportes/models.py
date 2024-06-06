from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


## Modelo para reportes de publicaciones
class Reporte(models.Model):
    MOTIVOS_REPORTE = [
        ('SPAM', 'Spam'),
        ('INAPROPIADO', 'Contenido inapropiado'),
        ('FRAUDE', 'Contenidoo fraudulento'),
        ('OTRO', 'Otro'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    motivo = models.CharField(choices=MOTIVOS_REPORTE, max_length=20)
    descripcion = models.TextField(null=False, blank=False)
    fecha_reporte = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Reportes"

    def __str__(self):
        return f"{self.usuario} reportó {self.content_object} por {self.motivo}"