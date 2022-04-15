from django.urls import path
# importar la HolaApiView de las vistas de profile_api
from profiles_api.views import HolaApiView

urlpatterns = [
    path('hola-view/', HolaApiView.as_view())
]