from django.contrib import admin
from .models import ReporteMascota, ReporteEvento, ReporteServicio

class ReporteMascotaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'mascota', 'motivo', 'descripcion', 'estado', 'fecha_reporte')
    readonly_fields = ('usuario', 'mascota', 'motivo', 'descripcion', 'fecha_reporte')
    
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.readonly_fields + ('estado',)
        return self.readonly_fields

class ReporteEventoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'evento', 'motivo', 'descripcion', 'estado', 'fecha_reporte')
    readonly_fields = ('usuario', 'evento', 'motivo', 'descripcion', 'fecha_reporte')
    
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.readonly_fields + ('estado',)
        return self.readonly_fields

class ReporteServicioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'servicio', 'motivo', 'descripcion', 'estado', 'fecha_reporte')
    readonly_fields = ('usuario', 'servicio', 'motivo', 'descripcion', 'fecha_reporte')
    
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.readonly_fields + ('estado',)
        return self.readonly_fields

admin.site.register(ReporteMascota, ReporteMascotaAdmin)
admin.site.register(ReporteEvento, ReporteEventoAdmin)
admin.site.register(ReporteServicio, ReporteServicioAdmin)
