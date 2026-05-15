from django.db import models
from django.conf import settings
from Peliculas.model.pelicula_model import Pelicula


class Review(models.Model):
    # le digo que utilice el modelo que configure en settings.py
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    texto = models.TextField()

    puntuacion = models.DecimalField(max_digits=2,decimal_places=1)
    fecha = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.usuario} - {self.pelicula.name}"