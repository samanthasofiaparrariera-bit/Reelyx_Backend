from django.contrib import admin
from Reviews.model.reviews_model import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'pelicula', 'puntuacion', 'fecha')
    list_filter = ('puntuacion', 'fecha')

admin.site.register(Review, ReviewAdmin)