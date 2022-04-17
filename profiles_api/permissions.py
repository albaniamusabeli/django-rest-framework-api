## crear permisos para que solo clientes registrados puedan editar su perfil
from rest_framework import permissions

class ActualizarPropioPerfil(permissions.BasePermission):
    """ Permite al usuario editar su propio perfil """
    
    def has_object_permission(self, request, view, obj):
        """Chequear si el usuario esta intentando editar su propio perfil"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        ## comparar si el usuario logueado esta actualizando sus datos
        return obj.id == request.user.id