from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.register_serializer import RegisterSerializer
# no entiendo por qué no me funciona voy a llorar
# update: ahora si lo entiendo :)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True}, status=status.HTTP_201_CREATED)

        return Response({"success":False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)