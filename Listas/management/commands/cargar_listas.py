from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from Listas.model.listas_model import Lista
from Peliculas.model.pelicula_model import Pelicula


class Command(BaseCommand):
    help = "Carga listas iniciales en la base de datos"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        usuario = User.objects.first()

        if not usuario:
            self.stdout.write("No hay usuarios. Crea primero un usuario o superusuario.")
            return

        listas = [
            {
                "nombre": "Favoritas para ver en invierno",
                "descripcion": "Películas con ambientes tranquilos, emocionales o misteriosos.",
                "peliculas": ["Bajo la misma lluvia", "La casa del umbral", "Sombra doble"],
            },
            {
                "nombre": "Aventuras y mundos fantásticos",
                "descripcion": "Historias de fantasía, exploración y mundos imaginarios.",
                "peliculas": ["El club de las nubes", "El reino de ceniza", "La ciudad perdida del sol"],
            },
            {
                "nombre": "Películas con mucha acción",
                "descripcion": "Selección de películas con ritmo rápido y tensión.",
                "peliculas": ["Límite de impacto", "Órbita cero", "Sombra doble"],
            },
            {
                "nombre": "Para ver con amigos",
                "descripcion": "Películas ligeras, entretenidas y fáciles de recomendar.",
                "peliculas": ["Caos en el piso 7", "Doraemon", "El club de las nubes"],
            },
            {
                "nombre": "Top ciencia ficción",
                "descripcion": "Películas relacionadas con tecnología, espacio y futuros posibles.",
                "peliculas": ["Órbita cero", "Límite de impacto", "La ciudad perdida del sol"],
            },
            {
                "nombre": "Mis imprescindibles",
                "descripcion": "Lista personal con algunas de las películas mejor valoradas.",
                "peliculas": ["Órbita cero", "Doraemon", "Bajo la misma lluvia", "El reino de ceniza"],
            },
        ]

        for data in listas:
            lista, created = Lista.objects.update_or_create(
                usuario=usuario,
                nombre=data["nombre"],
                defaults={
                    "descripcion": data["descripcion"]
                }
            )

            peliculas = Pelicula.objects.filter(name__in=data["peliculas"])
            lista.peliculas.set(peliculas)

            estado = "Creada" if created else "Actualizada"
            self.stdout.write(f"{estado}: {lista.nombre}")