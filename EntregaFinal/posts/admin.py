from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "pelicula", "genero", "puntuacion", "autor", "fecha_creacion")
    list_filter = ("genero", "puntuacion", "autor", "fecha_creacion")
    search_fields = ("titulo", "pelicula", "contenido")
    readonly_fields = ("slug",)
