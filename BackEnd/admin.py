from django.contrib import admin
from BackEnd.models import *


class PaisAdmin(admin.ModelAdmin):

    list_display = ['id', 'nombre_pais', ]
    list_filter = ['nombre_pais', ]

    fieldsets = (
        (
            'Detalle del país', {
                'classes': ['wide', ],
                'fields': ['nombre_pais', ]
            }
        ),
    )

    # readonly_fields = ['nombre_pais', ]

    ordering = search_fields = ['nombre_pais', ]


class CiudadAdmin(admin.ModelAdmin):

    list_display = ['id', 'nombre_ciudad', 'pais', ]
    list_filter = ['nombre_ciudad', 'pais', ]

    fieldsets = (
        (
            'Detalle de la ciudad', {
                'classes': ['wide', ],
                'fields': ['nombre_ciudad', 'pais', ]
            }
        ),
    )

    # readonly_fields = ['nombre_ciudad', 'pais', ]

    search_fields = ['nombre_ciudad', 'pais__nombre_pais', ]
    ordering = ['pais', ]


class TemperaturaHumedadAdmin(admin.ModelAdmin):

    list_display = ['ciudad', 'fecha_registro', ]
    list_filter = ['ciudad', 'fecha_registro', ]

    fieldsets = (
        (
            'Lugar de captura', {
                'classes': ['wide', ],
                'fields': ['ciudad', 'fecha_registro', ]
            }
        ),
        (
            'Datos obtenidos', {
                'classes': ['wide', ],
                'fields': ['temperatura', 'humedad', ]
            }
        ),
    )

    readonly_fields = ['ciudad', 'fecha_registro', 'temperatura', 'humedad', ]

    search_fields = ['ciudad__nombre_ciudad', 'ciudad__pais__nombre_pais', ]
    ordering = ['fecha_registro', ]


admin.site.register(Pais, PaisAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(TemperaturaHumedad, TemperaturaHumedadAdmin)
