from django.urls import path
from .views import (
    Reportar,
    Reportes
)

urlpatterns = [
    path('reportar/<int:pk>', Reportar.as_view(), name='crear-reporte'),
    path('reportes/', Reportes.as_view(), name='list-reporte'),
]
