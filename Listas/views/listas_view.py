from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Listas.model.listas_model import Lista
from Listas.serializers.listas_serializers import ListaSerializer, ListaDetalleSerializer
from rest_framework.permissions import AllowAny
# Proyecto: Reelyx
# Autora: Samantha Sofía Parra Riera
# Descripción: Vista encargada de crear, mostrar, editar y eliminar listas de películas.

class ListasView(APIView):
    permission_classes = [AllowAny]

    # Solo usuarios autenticados pueden crear listas
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({
                "error": "Debes iniciar sesión para crear una lista"
            }, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ListaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(usuario=request.user)

            return Response({"success": True, "data": serializer.data
                             }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Muestra todas las listas de todos los users
    def get(self, request):
        listas = Lista.objects.all().order_by('-creado')
        serializer = ListaDetalleSerializer(listas, many=True)

        return Response({"success": True, "data": serializer.data
                         }, status=status.HTTP_200_OK)

    # solo el dueño de la lista puede modificar (put) o eliminar (delete)
    def put(self, request, id):
        if not request.user.is_authenticated:
            return Response({
                "error": "Debes iniciar sesión para editar una lista"
            }, status=status.HTTP_401_UNAUTHORIZED)

        try:
            lista = Lista.objects.get(id=id)
        except Lista.DoesNotExist:
            return Response({
                "error": "Lista no encontrada"
            }, status=status.HTTP_404_NOT_FOUND)

        if lista.usuario != request.user:
            return Response({
                "error": "No puedes editar una lista que no es tuya"
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = ListaSerializer(lista, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(usuario=request.user)

            detalle = ListaDetalleSerializer(lista)

            return Response({
                "success": True,
                "data": detalle.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar lista
    def delete(self, request, id):
        # debe iniciar sesión para que funcione.
        if not request.user.is_authenticated:
            return Response({
                "error": "Debes iniciar sesión para eliminar una lista"
            }, status=status.HTTP_401_UNAUTHORIZED)

        try:
            lista = Lista.objects.get(id=id)
        except Lista.DoesNotExist:
            return Response({
                "error": "Lista no encontrada"
            }, status=status.HTTP_404_NOT_FOUND)

        if lista.usuario != request.user:
            return Response({
                "error": "No puedes eliminar una lista que no es tuya"
            }, status=status.HTTP_403_FORBIDDEN)

        lista.delete()

        return Response({"success": True, "message": "Lista eliminada correctamente"
                         }, status=status.HTTP_200_OK)
