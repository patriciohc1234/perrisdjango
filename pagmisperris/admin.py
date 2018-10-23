from django.contrib import admin
from .models import Persona
from .models import Mascota
from .models import MascotaPersona

admin.site.register(Persona)
admin.site.register(Mascota)
admin.site.register(MascotaPersona)