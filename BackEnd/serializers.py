from rest_framework import serializers

from BackEnd.models import *


# Pais Serializer
class PaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pais
        fields = ['nombre_pais']


# Ciudad Serializer
class CiudadSerializer(serializers.ModelSerializer):

    pais = serializers.CharField(source='pais.nombre_pais', read_only=True)

    class Meta:
        model = Ciudad
        fields = [
            'nombre_ciudad',
            'pais'
        ]


# TemperaturaHumedad Serializer
class TemperaturaHumedadSerializer(serializers.ModelSerializer):

    ciudad = serializers.CharField(source='ciudad.nombre_ciudad', read_only=True)
    pais = serializers.CharField(source='ciudad.pais.nombre_pais', read_only=True)

    class Meta:
        model = TemperaturaHumedad
        fields = [
            'fecha_registro',
            'ciudad',
            'pais',
            'temperatura',
            'humedad'
        ]
