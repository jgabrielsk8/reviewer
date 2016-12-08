from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Review
from .serializers import ReviewSerializer


class ReviewList(APIView):
    """
    List all reviews, or create a new review.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        reviews = Review.objects.filter(reviewer=request.user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
