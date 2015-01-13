# -*- encoding: utf-8 -*-

from django.contrib import admin
from imagekit.admin import AdminThumbnail

from .models import Player, Entrada

class EntradaAdmin(admin.ModelAdmin):
    miniatura = AdminThumbnail(image_field='thumb_admin')
    list_display = ['title', 'miniatura']


admin.site.register(Player)
admin.site.register(Entrada, EntradaAdmin)
