from rest_framework import routers
from BackEnd.api import *

router = routers.DefaultRouter()

router.register('api/pais', PaisViewSet, 'pais')
router.register('api/ciudad', CiudadViewSet, 'ciudad')
router.register('api/temperatura-humedad', TemperaturaHumedadViewSet, 'temperaturahumedad')

urlpatterns = router.urls
