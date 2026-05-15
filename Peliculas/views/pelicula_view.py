from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..model.pelicula_model import Pelicula
from Peliculas.serializers import PeliculaSerializer

class PeliculaView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        peliculas = Pelicula.objects.all()
        serializer = PeliculaSerializer(peliculas, many=True)
        data = []
        for pelicula in peliculas:
            data.append({
                "id": pelicula.id,
                "name": pelicula.name,
                "year": pelicula.year,
                "genre": pelicula.genre,
                "duration": pelicula.duration,
                "rating": pelicula.rating,
                "imagen": request.build_absolute_uri(pelicula.image.url),
                "sinopsis":pelicula.sinopsis,
            })
        return Response({"success": True, "data": data}, status=status.HTTP_200_OK)

