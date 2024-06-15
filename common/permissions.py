from rest_framework.permissions import BasePermission


## ADMINISTRACION DE PERMISOS POR TIPO DE USUARIOS
# Permisos para Persona u Organizacion
class IsPersonaOrOrganizacion(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_persona or request.user.is_organizacion)


# Permisos sólo para Organizacion
class IsOrganizacion(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_organizacion


# Permisos para Administrador
class IsAdministrador(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)


# Permisos para Cualquier tipo de usuario
class IsOwnerOrAdministrador(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.usuario or request.user.is_staff or request.user.is_superuser
