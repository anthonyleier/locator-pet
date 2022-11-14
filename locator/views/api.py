from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from locator.models import Post
from locator.serializers import PostSerializer


class Paginator(PageNumberPagination):
    page_size = 2


class PostList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.filter(author=request.user).select_related('author')
        serializer = PostSerializer(instance=posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class PostDetail(APIView):
    permission_classes = [IsAuthenticated]

    def getPost(self, user, id):
        post = get_object_or_404(Post.objects.filter(author=user), id=id)
        return post

    def get(self, request, id):
        post = self.getPost(request.user, id)
        serializer = PostSerializer(instance=post)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        post = self.getPost(request.user, id)
        serializer = PostSerializer(instance=post, data=request.data, many=False, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        post = self.getPost(request.user, id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
