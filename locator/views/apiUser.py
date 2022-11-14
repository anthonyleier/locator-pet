from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from locator.serializers import UserSerializer


class UserList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(instance=request.user, many=False)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        serializer = UserSerializer(instance=request.user, many=False)
        return Response(serializer.data)

    def patch(self, request, id):
        serializer = UserSerializer(instance=request.user, data=request.data, many=False, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
