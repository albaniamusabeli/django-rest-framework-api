from rest_framework.views import APIView
from rest_framework.response import Response


class HolaApiView(APIView):
    """ API View de prueba"""

    def get(self, request, format=None):
        ## Retornar lista de caracteristicas del API View
        api_view = [
            'Usamos metodos HTTP como funciones (get, post, put, delete, patch)',
            'Es similar a una vista tradicional de Django',
            'Da mayor control sobre la logica de la aplicacion'

        ]
        # transformar la info a JSON
        return Response({'mensaje':'Hola', 'api_view':api_view})