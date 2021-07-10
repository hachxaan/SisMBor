from django.contrib import admin

# Register your models here.
import OBTaller.models

admin.site.register(OBTaller.models.ConceptoTipo)
admin.site.register(OBTaller.models.Operacion)
admin.site.register(OBTaller.models.PeriodoKm)
admin.site.register(OBTaller.models.ConceptoCategoria)
admin.site.register(OBTaller.models.ConceptoMarca)
