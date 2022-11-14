from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from django.shortcuts import get_object_or_404

from locator.models import Post
from locator.serializers import PostSerializer


class Paginator(PageNumberPagination):
    page_size = 2


class PostList(ListCreateAPIView):
    queryset = Post.objects.all().select_related('author')
    serializer_class = PostSerializer
    pagination_class = Paginator

    # def get(self, request):
    #     posts = Post.objects.all().select_related('author')
    #     serializer = PostSerializer(instance=posts, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = PostSerializer(data=request.data, many=False)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class PostDetail(APIView):
    def getPost(self, id):
        post = get_object_or_404(Post.objects.select_related('author'), id=id)
        return post

    def get(self, request, id):
        post = self.getPost(id)
        serializer = PostSerializer(instance=post)
        return Response(serializer.data)

    def patch(self, request, id):
        post = self.getPost(id)
        serializer = PostSerializer(instance=post, data=request.data, many=False, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        post = self.getPost(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
