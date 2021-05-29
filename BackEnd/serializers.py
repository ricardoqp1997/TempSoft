from rest_framework import serializers

from BackEnd.models import *


# Pais Serializer
class PaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pais
        fields = ['nombre_pais']


# Ciudad Serializer
class CiudadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ciudad
        fields = [
            'nombre_ciudad',
            'pais'
        ]


# TemperaturaHumedad Serializer
class TemperaturaHumedadSerializer(serializers.ModelSerializer):

    class Meta:
        model = TemperaturaHumedad
        fields = [
            'ciudad',
            'temperatura',
            'humedad'
        ]
