from rest_framework import serializers

class HolaSerializer(serializers.Serializer):
    # Serializar un campo para probar la APIView
    name = serializers.CharField(max_length=10)