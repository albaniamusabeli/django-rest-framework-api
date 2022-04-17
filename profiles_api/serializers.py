from rest_framework import serializers
from profiles_api.models import UserProfile


class HolaSerializer(serializers.Serializer):
    # Serializar un campo para probar la APIView
    name = serializers.CharField(max_length=10)


## Serializador del perfil de usuario
class UserProfileSerializer(serializers.ModelSerializer):
    ## Serializa un objeto del perfil de usuario

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        ## para proteger la clave: extra_kwargs
        extra_kwargs = {
            'password':{
                'write_only': True,## solo ver la clave cuando se esta registrando un nuevo usuario
                'style': {'input_type':'password'} ## estilizar la clave como asterisco
            }
        }
    
    # para sobreescribir una funcion
    def create(self, validated_data):
        ## Crear y retornar nuevo usuario
        user = UserProfile.objects.create_user(
            email=validated_data['email'],## validar email
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
    
    ## para actualizar cuenta de usuario
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
