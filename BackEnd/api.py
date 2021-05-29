from rest_framework import viewsets, permissions

from BackEnd.serializers import *


# Pais ViewSet
class PaisViewSet(viewsets.ModelViewSet):

    queryset = Pais.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = PaisSerializer


# Ciudad ViewSet
class CiudadViewSet(viewsets.ModelViewSet):

    queryset = Ciudad.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = CiudadSerializer


# TemperaturaHumedad ViewSet
class TemperaturaHumedadViewSet(viewsets.ModelViewSet):

    queryset = TemperaturaHumedad.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = TemperaturaHumedadSerializer
