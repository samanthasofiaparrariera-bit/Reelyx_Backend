from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from Users.models.users_models import CustomUser
from Users.serializers.profile_serializer import ProfileSerializer

class PublicProfileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, email):
        try:
            usuario = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"error": "Usuario no encontrado"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(usuario)
        return Response({"success": True,"data": serializer.data
        }, status=status.HTTP_200_OK)