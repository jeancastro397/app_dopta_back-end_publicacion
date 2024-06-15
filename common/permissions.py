from rest_framework.permissions import BasePermission

class IsPersonaOrOrganizacion(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_persona or request.user.is_organizacion)

class IsOrganizacion(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_organizacion

class IsAdministrador(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_administrador

class IsOwnerOrAdministrador(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.usuario or request.user.is_administrador
