from rest_framework import serializers
from Listas.model.listas_model import Lista
from Peliculas.model.pelicula_model import Pelicula


class ListaSerializer(serializers.ModelSerializer):
    peliculas = serializers.PrimaryKeyRelatedField( many=True,
        queryset=Pelicula.objects.all())

    class Meta:
        model = Lista
        fields = ('id', 'nombre', 'descripcion', 'peliculas')

    # Esta función se asegura de que no hay más de 30 películas
    def validate_peliculas(self, peliculas):
        if len(peliculas) > 30:
            raise serializers.ValidationError("No se puede añadir más de 30 películas")

        return peliculas

    def create(self, validated_data):
        peliculas = validated_data.pop('peliculas')
        usuario = validated_data.pop('usuario')

        lista = Lista.objects.create(
            usuario=usuario,
            nombre=validated_data['nombre'],
            descripcion=validated_data.get('descripcion', ''),
        )

        lista.peliculas.set(peliculas)

        return lista

class ListaDetalleSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.nombre', read_only=True)
    usuario_email = serializers.CharField(source='usuario.email', read_only=True)
    usuario_pfp = serializers.ImageField(source='usuario.image', read_only=True)
    cantidad_peliculas = serializers.IntegerField(source='numPelis', read_only=True)

    peliculas_detalle = serializers.SerializerMethodField()

    class Meta:
        model = Lista
        fields = (
            'id',
            'nombre',
            'descripcion',
            'usuario_nombre',
            'usuario_email',
            'usuario_pfp',
            'cantidad_peliculas',
            'peliculas_detalle',
            'creado'
        )

    def get_peliculas_detalle(self, lista):
        peliculas = []

        for peli in lista.peliculas.all():
            peliculas.append({
                "id": peli.id,
                "name": peli.name,
                "imagen": peli.image.url if peli.image else "",
                "genre": peli.genre,
                "year": peli.year,
            })

        return peliculas