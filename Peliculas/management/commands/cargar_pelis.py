from django.core.management.base import BaseCommand
from Peliculas.model.pelicula_model import Pelicula


class Command(BaseCommand):
    help = "Carga películas iniciales en la base de datos"

    def handle(self, *args, **kwargs):
        pelis = [
            {
                "name": "Bajo la misma lluvia",
                "image": "peliculas/bajo-la-misma-lluvia.jpg",
                "duration": 2,
                "genre": "romance",
                "year": 2022,
                "rating": 4.1,
                "sinopsis": "Dos antiguos amantes se reencuentran en una "
                            "ciudad marcada por la lluvia constante. Durante unos días, deberán enfrentarse"
                            " a decisiones del pasado mientras redescubren lo que realmente sienten el uno por el otro.",
            },
            {
                "name": "Caos en el piso 7",
                "image": "peliculas/caos-en-el-piso-7.jpg",
                "duration": 2,
                "genre": "comedia",
                "year": 2021,
                "rating": 3.8,
                "sinopsis": "Un tranquilo edificio se convierte"
                            " en un completo desastre cuando nuevos vecinos excéntricos llegan al"
                            " séptimo piso, provocando situaciones absurdas que pondrán patas arriba la vida de todos.",
            },
            {
                "name": "Doraemon",
                "image": "peliculas/doraemon.jpg",
                "duration": 2,
                "genre": "animacion",
                "year": 2019,
                "rating": 4.5,
                "sinopsis": "Nobita recibe la ayuda de Doraemon,"
                            " un gato robótico del futuro, para mejorar su vida. Sin embargo,"
                            " cada invento trae consecuencias inesperadas que le enseñarán importantes lecciones.",
            },
            {
                "name": "El club de las nubes",
                "image": "peliculas/el-club-de-las-nubes.jpg",
                "duration": 2,
                "genre": "fantasia",
                "year": 2023,
                "rating": 4.0,
                "sinopsis": "Un grupo de niños descubre un mundo secreto entre las nubes donde todo es posible."
                            " Juntos deberán proteger ese lugar mágico de una amenaza "
                            "que busca destruir su equilibrio.",
            },
            {
                "name": "El reino de ceniza",
                "image": "peliculas/el-reino-de-ceniza.jpg",
                "duration": 3,
                "genre": "fantasia",
                "year": 2020,
                "rating": 4.3,
                "sinopsis": "Tras la caída de un imperio, una joven "
                            "heredera debe recuperar el trono perdido en un mundo devastado por la guerra, "
                            "enfrentándose a criaturas oscuras y traiciones inesperadas.",
            },
            {
                "name": "La casa del umbral",
                "image": "peliculas/la-casa-del-umbral.jpg",
                "duration": 2,
                "genre": "terror",
                "year": 2024,
                "rating": 3.9,
                "sinopsis": "Una familia se muda a una antigua casa donde "
                            "comienzan a suceder fenómenos inexplicables."
                            " Pronto descubrirán que han cruzado un umbral del que no podrán escapar fácilmente.",
            },
            {
                "name": "La ciudad perdida del sol",
                "image": "peliculas/la-ciudad-perdida-del-sol.jpg",
                "duration": 3,
                "genre": "aventura",
                "year": 2021,
                "rating": 4.4,
                "sinopsis": "Un arqueólogo emprende una peligrosa "
                            "expedición en busca de una civilización olvidada que podría "
                            "cambiar la historia, enfrentándose a trampas mortales y enemigos sin escrúpulos.",
            },
            {
                "name": "Límite de impacto",
                "image": "peliculas/limite-de-impacto.jpg",
                "duration": 2,
                "genre": "accion",
                "year": 2023,
                "rating": 4.2,
                "sinopsis": "Un agente especial debe detener una amenaza global antes de "
                            "que sea demasiado tarde, enfrentándose a una carrera contrarreloj"
                            " llena de explosiones, persecuciones y giros inesperados.",
            },
            {
                "name": "Órbita cero",
                "image": "peliculas/orbita-cero.jpg",
                "duration": 2,
                "genre": "sci_fi",
                "year": 2025,
                "rating": 4.6,
                "sinopsis": "Una misión espacial se convierte en una lucha por"
                            " la supervivencia cuando la tripulación pierde contacto "
                            "con la Tierra y descubre que no están solos en el espacio.",
            },
            {
                "name": "Sombra doble",
                "image": "peliculas/sombra-doble.jpg",
                "duration": 2,
                "genre": "thriller",
                "year": 2022,
                "rating": 4.0,
                "sinopsis": "Un detective investiga una serie de crímenes "
                            "que parecen estar conectados con su propio pasado,"
                            " descubriendo una verdad que pondrá en duda su identidad.",
            },
        ]

        for data in pelis:
            pelicula, created = Pelicula.objects.update_or_create(
                name=data["name"],
                defaults=data
            )

            estado = "Creada" if created else "Actualizada"
            self.stdout.write(f"{estado}: {pelicula.name}")
