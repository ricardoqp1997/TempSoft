from rest_framework import viewsets, permissions
from rest_framework.response import Response

from BackEnd.serializers import *


# Pais ViewSet
class PaisViewSet(viewsets.ModelViewSet):

    serializer_class = PaisSerializer

    def get_queryset(self):

        pais = Pais.objects.all()
        return pais

    # GET
    def retrieve(self, request, *args, **kwargs):

        params = kwargs
        print(params['pk'])

        try:
            pais = Pais.objects.filter(id=params['pk'])
            serializer = PaisSerializer(pais, many=True)

            return Response(serializer.data)

        except:
            pais = Pais.objects.filter(nombre_pais=params['pk'])
            serializer = PaisSerializer(pais, many=True)

            return Response(serializer.data)

    # POST
    def create(self, request, *args, **kwargs):

        pais_data = request.data

        if Pais.objects.filter(nombre_pais=pais_data['nombre_pais']):
            return Response(
                {'message': 'Este país ya se encuentra registrado'}
            )

        else:
            new_pais = Pais.objects.create(
                nombre_pais=pais_data['nombre_pais']
            )

            new_pais.save()

            serializer = PaisSerializer(new_pais)
            print(serializer)

            return Response(
                {'message': f'Se ha registrado correctamente el país: {pais_data["nombre_pais"]}'}
            )

    # DELETE
    def destroy(self, request, *args, **kwargs):

        params = kwargs
        print(f'-> {params["pk"]}')

        try:
            pais = Pais.objects.filter(id=params["pk"])
            pais.delete()

            return Response(
                {'message': 'Se ha eliminado correctamente el país'}
            )

        except:
            pais = Pais.objects.filter(nombre_pais=params["pk"])
            pais.delete()

            return Response(
                {'message': 'Se ha eliminado correctamente el país'}
            )

    # UPDATE
    def update(self, request, *args, **kwargs):

        params = kwargs
        print(f'-> {params["pk"]}')

        pais_data = request.data

        try:
            pais = Pais.objects.filter(id=params["pk"])
            print(pais)
            pais.update(nombre_pais=pais_data['nombre_pais'])

            return Response(
                {'message': 'Se ha actualizado correctamente el país'}
            )

        except:
            pais = Pais.objects.filter(nombre_pais=params["pk"])
            print(pais)
            pais.update(nombre_pais=pais_data['nombre_pais'])

            return Response(
                {'message': 'Se ha actualizado correctamente el país'}
            )

    permission_classes = [
        permissions.AllowAny
    ]


# Ciudad ViewSet
class CiudadViewSet(viewsets.ModelViewSet):

    serializer_class = CiudadSerializer

    def get_queryset(self):

        ciudad = Ciudad.objects.all()
        return ciudad

    # GET
    def retrieve(self, request, *args, **kwargs):

        params = kwargs
        print(params['pk'])

        try:
            ciudad = Ciudad.objects.filter(id=params['pk'])
            serializer = CiudadSerializer(ciudad, many=True)

            return Response(serializer.data)

        except:
            ciudad = Ciudad.objects.filter(nombre_ciudad=params['pk'])
            serializer = CiudadSerializer(ciudad, many=True)

            return Response(serializer.data.pop())

    # POST
    def create(self, request, *args, **kwargs):

        ciudad_data = request.data
        print(ciudad_data)

        if Ciudad.objects.filter(nombre_ciudad=ciudad_data['nombre_ciudad']):
            return Response(
                {'message': f'Esta ciudad ya se encuentra registrada'}
            )

        else:

            if not Pais.objects.filter(nombre_pais=ciudad_data['pais']):
                new_pais = Pais.objects.create(nombre_pais=ciudad_data['pais'])
                new_pais.save()

                pais = Pais.objects.get(nombre_pais=ciudad_data['pais'])

            else:
                pais = Pais.objects.get(nombre_pais=ciudad_data['pais'])

            new_ciudad = Ciudad.objects.create(
                nombre_ciudad=ciudad_data['nombre_ciudad'],
                pais=pais
            )

            new_ciudad.save()

            serializer = CiudadSerializer(new_ciudad)
            print(serializer)

            return Response(
                {'message': f'Se ha registrado correctamente la ciudad: {ciudad_data["nombre_ciudad"]}'}
            )

    # DELETE
    def destroy(self, request, *args, **kwargs):

        params = kwargs
        print(f'-> {params["pk"]}')

        try:
            ciudad = Ciudad.objects.filter(id=params["pk"])
            ciudad.delete()

            return Response(
                {'message': 'Se ha eliminado correctamente la ciudad'}
            )

        except:
            ciudad = Ciudad.objects.filter(nombre_ciudad=params["pk"])
            ciudad.delete()

            return Response(
                {'message': 'Se ha eliminado correctamente la ciudad'}
            )

    # UPDATE
    def update(self, request, *args, **kwargs):

        params = kwargs
        print(f'-> {params["pk"]}')

        ciudad_data = request.data

        if not Pais.objects.filter(nombre_pais=ciudad_data['pais']):
            new_pais = Pais.objects.create(nombre_pais=ciudad_data['pais'])
            new_pais.save()

            pais = Pais.objects.get(nombre_pais=ciudad_data['pais'])

        else:
            pais = Pais.objects.get(nombre_pais=ciudad_data['pais'])

        try:
            ciudad = Ciudad.objects.filter(id=params["pk"])
            print(ciudad)
            ciudad.update(nombre_ciudad=ciudad_data['nombre_ciudad'])
            ciudad.update(pais=pais)

            return Response(
                {'message': 'Se ha actualizado correctamente la ciudad'}
            )

        except:
            ciudad = Ciudad.objects.filter(nombre_ciudad=params["pk"])
            print(ciudad)
            ciudad.update(nombre_ciudad=ciudad_data['nombre_ciudad'])
            ciudad.update(pais=pais)

            return Response(
                {'message': 'Se ha actualizado correctamente la ciudad'}
            )


# TemperaturaHumedad ViewSet
class TemperaturaHumedadViewSet(viewsets.ModelViewSet):

    serializer_class = TemperaturaHumedadSerializer

    def get_queryset(self):

        temperatura_humedad = TemperaturaHumedad.objects.all()
        return temperatura_humedad

    # GET
    def retrieve(self, request, *args, **kwargs):

        params = kwargs
        print(params['pk'])

        try:
            ciudad = Ciudad.objects.get(nombre_ciudad=params['pk'])
            temperatura_humedad = TemperaturaHumedad.objects.filter(ciudad=ciudad)
            serializer = TemperaturaHumedadSerializer(temperatura_humedad, many=True)

            return Response(serializer.data)

        except:
            ciudad = Ciudad.objects.get(id=params['pk'])
            temperatura_humedad = TemperaturaHumedad.objects.filter(ciudad=ciudad)
            serializer = CiudadSerializer(temperatura_humedad, many=True)

            return Response(serializer.data.pop())

    # POST
    def create(self, request, *args, **kwargs):
        print('aaaaa')
        temperatura_humedad_data = request.data
        print(temperatura_humedad_data)

        # Verificamos existencia de pais
        if not Pais.objects.filter(nombre_pais=temperatura_humedad_data['pais']):
            new_pais = Pais.objects.create(nombre_pais=temperatura_humedad_data['pais'])
            new_pais.save()

            pais = Pais.objects.get(nombre_pais=temperatura_humedad_data['pais'])

        else:
            pais = Pais.objects.get(nombre_pais=temperatura_humedad_data['pais'])

        # Verificamos existencia de ciudad
        if not Ciudad.objects.filter(nombre_ciudad=temperatura_humedad_data['ciudad']):
            mew_ciudad = Ciudad.objects.create(nombre_ciudad=temperatura_humedad_data['ciudad'], pais=pais)
            mew_ciudad.save()

            ciudad = Ciudad.objects.get(nombre_ciudad=temperatura_humedad_data['ciudad'])

        else:
            ciudad = Ciudad.objects.get(nombre_ciudad=temperatura_humedad_data['ciudad'])

        new_temperatura_humedad = TemperaturaHumedad.objects.create(
            ciudad=ciudad,
            temperatura=temperatura_humedad_data['temperatura'],
            humedad=temperatura_humedad_data['humedad']
        )

        new_temperatura_humedad.save()

        serializer = CiudadSerializer(new_temperatura_humedad)
        print(serializer)

        return Response(
            {'message': f'Se ha registrado correctamente la temperatura y humedad en: {temperatura_humedad_data["ciudad"]}'}
        )

    # DELETE
    def destroy(self, request, *args, **kwargs):

        params = kwargs
        print(f'-> {params["pk"]}')

        try:
            ciudad = Ciudad.objects.filter(id=params["pk"])
            ciudad.delete()

            return Response(
                {'message': 'Se ha eliminado correctamente la ciudad'}
            )

        except:
            ciudad = Ciudad.objects.filter(nombre_ciudad=params["pk"])
            ciudad.delete()

            return Response(
                {'message': 'Se ha eliminado correctamente la ciudad'}
            )

    # UPDATE
    def update(self, request, *args, **kwargs):

        params = kwargs
        print(f'-> {params["pk"]}')

        ciudad_data = request.data

        if not Pais.objects.filter(nombre_pais=ciudad_data['pais']):
            new_pais = Pais.objects.create(nombre_pais=ciudad_data['pais'])
            new_pais.save()

            pais = Pais.objects.get(nombre_pais=ciudad_data['pais'])

        else:
            pais = Pais.objects.get(nombre_pais=ciudad_data['pais'])

        try:
            ciudad = Ciudad.objects.filter(id=params["pk"])
            print(ciudad)
            ciudad.update(nombre_ciudad=ciudad_data['nombre_ciudad'])
            ciudad.update(pais=pais)

            return Response(
                {'message': 'Se ha actualizado correctamente la ciudad'}
            )

        except:
            ciudad = Ciudad.objects.filter(nombre_ciudad=params["pk"])
            print(ciudad)
            ciudad.update(nombre_ciudad=ciudad_data['nombre_ciudad'])
            ciudad.update(pais=pais)

            return Response(
                {'message': 'Se ha actualizado correctamente la ciudad'}
            )
