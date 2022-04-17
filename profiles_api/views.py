from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers, models


class HolaApiView(APIView):
    # API View de prueba

    # Crear serializers_class para tener acceso al serializer que creamos (HolaSerializer)
    serializers_class = serializers.HolaSerializer

    ## metodo get para obtener datos
    def get(self, request, format=None):
        ## Retornar lista de caracteristicas del API View
        api_view = [
            'Usamos metodos HTTP como funciones (get, post, put, delete, patch)',
            'Es similar a una vista tradicional de Django',
            'Da mayor control sobre la logica de la aplicacion'

        ]
        # transformar la info a JSON
        return Response({'mensaje':'Hola', 'api_view':api_view})


    ## metodo para enviar datos con request
    def post(self, request):
        ## Crea un mensaje con nuestro name que creamos en serializer.py
        serializer = self.serializers_class(data=request.data)

        ## validar el serializer
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            mensaje = f'Hello {name}'
            return Response({'mensaje': mensaje})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    

    ## metodo para actualizar un objeto
    def put(self, request, pk=None):
        return Response({'method':'PUT'})
    

    ## metodo para actualizacion parcial un objeto
    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})


    ## metodo para borrar un registro
    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})

    
### CREAR VIEWSETS
class HolaViewSet(viewsets.ViewSet):

    serializers_class = serializers.HolaSerializer

    ## Listar los objetos (como un GET)
    def list(self, request):
        # Retornar mensaje de hola Mundo
        api_viewset = [
            'Usa acciones (list, create, retrieve, update, partial_update)',
            'Automaticamente mapea a los URLs usando Routers',
            'Provee mas funcionalidad con menos código'
        ]
        return Response({'mensaje': 'Hola!', 'api_viewset': api_viewset})
    
    
    # Crear nuevo mensaje de Hola Mundo (es como el POST)
    def create(self, request):

        serializer = self.serializers_class(data=request.data)

        # Verificar que la informacion recibida es valida
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            mensaje = f"Hola {name}"
            return Response({'mensaje': mensaje})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    

    ## Obtener un solo dato segun su PK o ID
    def retrieve(self, request, pk=None):
        return Response({'metodo_http':'GET'})


    ## Actualizar
    def update(self, request, pk=None):
        return Response({'metodo_http':'PUT'})


    ## Eliminar
    def destroy(self, request, pk=None):
        return Response({'metodo_http':'DELETE'})
    

## LA TABLA DE USUARIO SE VA A CONVERTIR EN JSON PARA REGISTRAR Y/O LISTAR
class UserProfileViewSet(viewsets.ModelViewSet):
    """ Crear y actualizar perfiles """
    ## Convertir en JSON la tabla UserProfile (serializer_class debe llamarse asi, porque es de django)
    serializer_class = serializers.UserProfileSerializer
    ## Crear una consulta para obtener todos los usuarios
    queryset = models.UserProfile.objects.all()
    