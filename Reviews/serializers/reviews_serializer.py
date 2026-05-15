from rest_framework import serializers
from Reviews.model.reviews_model import Review
from Peliculas.model.pelicula_model import Pelicula


class ReviewSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='usuario.email', read_only=True)
    nombre_user = serializers.CharField(source='usuario.nombre', read_only=True)
    pfp = serializers.ImageField(source='usuario.image', read_only=True)

    name = serializers.CharField(source='pelicula.name', read_only=True)
    imagen = serializers.ImageField(source='pelicula.image', read_only=True)
    year = serializers.FloatField(source='pelicula.year', read_only=True)

    rating = serializers.DecimalField(source='puntuacion', max_digits=2, decimal_places=1, read_only=True)

    pelicula = serializers.PrimaryKeyRelatedField(
        queryset=Pelicula.objects.all(),
        write_only=True
    )

    puntuacion = serializers.DecimalField(
        max_digits=2,
        decimal_places=1,
        write_only=True
    )

    class Meta:
        model = Review
        fields = ('id','email', 'nombre_user','name','pfp',
            'imagen', 'texto','rating','year','pelicula','puntuacion',
        )