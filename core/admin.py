from django.contrib import admin
from .models import Cidade, TipoMusica, Imagem, Video, Local

admin.site.register(Cidade)
admin.site.register(Local)
admin.site.register(TipoMusica)
admin.site.register(Imagem)
admin.site.register(Video)
