from django.urls import path, include
# importar para los viewSets que estan el en views.py
from rest_framework.routers import DefaultRouter
# importar la HolaApiView de las vistas de profile_api
from profiles_api.views import HolaApiView, HolaViewSet, UserProfileViewSet



## Es necesario crear un router para los VIEWSETS y despues agregarlos a los PATH
router = DefaultRouter()
router.register('hola-viewset',HolaViewSet, basename='hola-viewset')
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('hola-view/', HolaApiView.as_view()),
    # registrar los router en el path
    path('', include(router.urls)) # Encuentra todos los URLs 
]