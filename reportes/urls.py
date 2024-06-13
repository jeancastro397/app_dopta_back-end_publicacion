from django.urls import path
from .views import (
    ReportarMascota,
    RemoveReporteMascota,
    ReportarEvento,
    RemoveReporteEvento,
    ReportarServicio,
    RemoveReporteServicio,
    ListReportesUsuario,
    ListReportesAdmin
)


urlpatterns = [
    # Endpoints de Reportes de Mascota
    path('reportar-pub-mascota/<int:pk>', ReportarMascota.as_view(), name='report-pub-mascota'),
    path('remover-reporte-mascota/<int:pk>', RemoveReporteMascota.as_view(), name='remove-report-mascota'),

    # Endpoints de Reportes de Evento
    path('reportar-pub-evento/<int:pk>', ReportarEvento.as_view(), name='report-pub-evento'),
    path('remover-reporte-evento/<int:pk>', RemoveReporteEvento.as_view(), name='remove-report-evento'),

    # Endpoints de Reportes de Servicio
    path('reportar-pub-servicio/<int:pk>', ReportarMascota.as_view(), name='report-pub-service'),
    path('remover-reporte-servicio/<int:pk>', RemoveReporteMascota.as_view(), name='remove-report-service'),

    # Endpoints de listas de reportes
    path('listar-reportes-usuario/', ListReportesUsuario.as_view(), name='list-report-user'),
    path('listar-reportes-admin/', ListReportesAdmin.as_view(), name='list-report-admin'),
]