from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from Reviews.model.reviews_model import Review
from Peliculas.model.pelicula_model import Pelicula


class Command(BaseCommand):
    help = "Carga reviews iniciales en la base de datos"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        usuario = User.objects.first()

        if not usuario:
            self.stdout.write("No hay usuarios. Crea primero un usuario o superusuario.")
            return

        reviews = [
            {
                "pelicula": "Bajo la misma lluvia",
                "texto": "Una película tranquila y emotiva, con una estética muy cuidada.",
                "puntuacion": 4.0,
            },
            {
                "pelicula": "Caos en el piso 7",
                "texto": "Divertida y ligera, ideal para ver sin demasiadas complicaciones.",
                "puntuacion": 3.5,
            },
            {
                "pelicula": "Doraemon",
                "texto": "Una historia agradable, familiar y con mucho encanto visual.",
                "puntuacion": 4.5,
            },
            {
                "pelicula": "El club de las nubes",
                "texto": "Tiene un mundo muy bonito y una atmósfera fantástica muy original.",
                "puntuacion": 4.0,
            },
            {
                "pelicula": "El reino de ceniza",
                "texto": "Una aventura de fantasía con buenos momentos y bastante intensidad.",
                "puntuacion": 4.2,
            },
            {
                "pelicula": "La casa del umbral",
                "texto": "Funciona bien como película de terror, con una ambientación inquietante.",
                "puntuacion": 3.8,
            },
            {
                "pelicula": "La ciudad perdida del sol",
                "texto": "Una película de aventura entretenida y visualmente llamativa.",
                "puntuacion": 4.3,
            },
            {
                "pelicula": "Límite de impacto",
                "texto": "Tiene buen ritmo y escenas de acción bastante efectivas.",
                "puntuacion": 4.1,
            },
            {
                "pelicula": "Órbita cero",
                "texto": "La parte de ciencia ficción está muy bien planteada y resulta atractiva.",
                "puntuacion": 4.6,
            },
            {
                "pelicula": "Sombra doble",
                "texto": "Un thriller interesante, con una historia que mantiene la tensión.",
                "puntuacion": 4.0,
            },
            {
                "pelicula": "Órbita cero",
                "texto": "Me gustó especialmente su estilo visual y la sensación de misterio.",
                "puntuacion": 4.4,
            },
            {
                "pelicula": "Bajo la misma lluvia",
                "texto": "Es sencilla, pero transmite muy bien la relación entre los personajes.",
                "puntuacion": 3.9,
            },
        ]

        for data in reviews:
            pelicula = Pelicula.objects.filter(name=data["pelicula"]).first()

            if not pelicula:
                self.stdout.write(f"No existe la película: {data['pelicula']}")
                continue

            review, created = Review.objects.update_or_create(
                usuario=usuario,
                pelicula=pelicula,
                texto=data["texto"],
                defaults={
                    "puntuacion": data["puntuacion"]
                }
            )

            estado = "Creada" if created else "Actualizada"
            self.stdout.write(f"{estado}: {pelicula.name}")