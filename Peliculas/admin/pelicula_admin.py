from django.contrib import admin
from ..model.pelicula_model import Pelicula

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'genre','rating','duration','image')
    list_filter = ('genre','year','rating','duration')
    search_fields = ('name',)
    readonly_fields = ('slug',)
    list_per_page = 50


admin.site.register(Pelicula, PeliculaAdmin)