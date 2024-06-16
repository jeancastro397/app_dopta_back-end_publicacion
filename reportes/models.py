from django.conf import settings
from django.db import models
from publicaciones.models import Mascota, Evento, Servicio

MOTIVOS_REPORTE = [
    ('SPAM', 'Spam'),
    ('INAPROPIADO', 'Contenido inapropiado'),
    ('FRAUDE', 'Contenido fraudulento'),
    ('OTRO', 'Otro'),
]

ESTADO_REPORTE = [
    ('ACEPTADO', 'Aceptado'),
    ('EN REVISION', 'En revisión'),
    ('RECHAZADO', 'Rechazado'),
]

# Models Reporte de publicacion Mascota
class ReporteMascota(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    motivo = models.CharField(choices=MOTIVOS_REPORTE, max_length=20)
    descripcion = models.TextField(null=False, blank=False, max_length=255)
    estado = models.CharField(choices=ESTADO_REPORTE, max_length=20, default='EN REVISION')
    fecha_reporte = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Reportes de Mascotas"

    def __str__(self):
        return f"{self.usuario.username} reportó por {self.motivo} a {self.mascota.usuario.username}"

# Models Reporte de publicacion Evento
class ReporteEvento(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    motivo = models.CharField(choices=MOTIVOS_REPORTE, max_length=20)
    descripcion = models.TextField(null=False, blank=False)
    estado = models.CharField(choices=ESTADO_REPORTE, max_length=20, default='EN REVISION')
    fecha_reporte = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Reportes de Eventos"

    def __str__(self):
        return f"{self.usuario.username} reportó por {self.motivo} a {self.evento.usuario.username}"

# Models Reporte de publicacion Servicio
class ReporteServicio(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    motivo = models.CharField(choices=MOTIVOS_REPORTE, max_length=20)
    descripcion = models.TextField(null=False, blank=False)
    estado = models.CharField(choices=ESTADO_REPORTE, max_length=20, default='EN REVISION')
    fecha_reporte = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Reportes de Servicios"

    def __str__(self):
        return f"{self.usuario.username} reportó por {self.motivo} a {self.servicio.usuario.username}"
