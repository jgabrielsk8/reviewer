from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from django.contrib.auth.models import User

from core.serializers import UserSerializer


class UserList(APIView):
    """
    List all users, or create a new user.
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        users = User.objects.filter()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        password = request.POST.get('password')
        serializer = UserSerializer(data=request.data, context={'password': password})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
