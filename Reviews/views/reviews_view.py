from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Reviews.model.reviews_model import Review
from Reviews.serializers.reviews_serializer import ReviewSerializer


class ReviewsView(APIView):
    def get(self, request):
        reviews = Review.objects.all().order_by('-fecha')
        serializer = ReviewSerializer(reviews, many=True)

        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({
                "error": "Debes iniciar sesión para escribir una reseña"
            }, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            review = serializer.save(usuario=request.user)

            respuesta = ReviewSerializer(review)

            return Response({
                "success": True,
                "data": respuesta.data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)