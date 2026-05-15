from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Users.serializers.profile_serializer import ProfileSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)

        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # Editar perfil, actualizar
    def put(self, request):
        user = request.user

        #  *** updateamos nombre
        if 'nombre' in request.data:
            user.nombre = request.data.get('nombre')

        # *** update bio
        if 'bio' in request.data:
            user.bio = request.data.get('bio')

        # *** imagen
        if 'image' in request.FILES:
            user.image = request.FILES['image']

        user.save()

        serializer = ProfileSerializer(user)

        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_200_OK)