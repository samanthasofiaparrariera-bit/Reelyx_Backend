import secrets

from django.db import models

from django.core.validators import FileExtensionValidator

class Pelicula(models.Model):
    name = models.CharField(max_length=70, blank=False, null=False)
    slug = models.SlugField(max_length=50, unique=True, blank=False, null=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    duration = models.DecimalField(max_digits=3, decimal_places=0)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    sinopsis = models.TextField(blank=True, default='')
    genre = models.CharField(max_length=50, blank=False, null=False,choices=[
        ('sci_fi', 'Sci-Fi'),
        ('romance', 'Romance'),
        ('drama', 'Drama'),
        ('accion', 'Acción'),
        ('comedia', 'Comedia'),
        ('terror', 'Terror'),
        ('aventura', 'Aventura'),
        ('fantasia', 'Fantasía'),
        ('animacion', 'Animación'),
        ('documental', 'Documental'),
        ('musical', 'Musical'),
        ('thriller', 'Thriller'),
    ])
    image = models.ImageField(upload_to="peliculas/", blank=False, null=False,
    validators=[FileExtensionValidator(['jpg', 'png'])])


    class Meta:
        ordering = ['rating', 'year']
        db_table = 'peliculas'
        verbose_name_plural = 'Peliculas'

    def __str__(self):
        return f"{self.name} - {self.year}"

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_hex(16)
            while Pelicula.objects.filter(slug=prov).exists():
                prov = secrets.token_hex(16)
            self.slug = prov
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)