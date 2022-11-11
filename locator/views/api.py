from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from locator.models import Post
from locator.serializers import PostSerializer


@api_view(http_method_names=['GET', 'POST'])
def postsList(request):
    if request.method == 'GET':
        posts = Post.objects.all().select_related('author')
        serializer = PostSerializer(instance=posts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['GET'])
def postDetail(request, id):
    post = get_object_or_404(Post.objects.select_related('author'), id=id)
    serializer = PostSerializer(instance=post)
    return Response(serializer.data)
