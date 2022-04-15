from django.db import models
from django.contrib.auth.models import AbstractBaseUser # Clase base de Django
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    ## Manager para perfiles de usuario
    def create_user(self, email, name, password=None):
        # Crear Nuevo usuario Profile
        if not email:
            raise ValueError('Usuario debe tener un email')

        # Metodo para pasar a minusculas el dominio del correo
        email = self.normalize_email(email)
        # el usuario va a tener los campos email y name
        user = self.model(email=email, name=name)
        # asegurarse que sea necesario una password
        user.set_password(password)
        # para poder guardar el usuario en la base de datos y que tenga un HASH
        user.save(using=self._db)

        return user
    
    # Este seria el usuario admin
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# Sobreescribir el modelo de USUARIO de Django (hacer login con el correo)
class UserProfile(AbstractBaseUser, PermissionsMixin):
    ## Modelo Base de datos para Usuarios en el sistema
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Crear para gestionar los usuarios (borrar, crear) --> modo manager
    objects = UserProfileManager()

    # USERNAME_FIELD sera el campo email, para que el usuario haga login con el EMAIL
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # Obtener nombre completo del usuario
    def get_full_name(self):
        return self.name

    # Obtener nombre corto del usuario
    def get_short_name(self):
        return self.name
    

    def __str__(self):
        # Retornar cadena representando nuestro usuario
        return self.email

''' Se debe registrar el UserProfile en el admin.py '''