from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from locator.models import Post
from locator.serializers import PostSerializer


@api_view(http_method_names=['GET'])
def postsList(request):
    posts = Post.objects.all().select_related('author')
    serializer = PostSerializer(instance=posts, many=True)
    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def postDetail(request, id):
    post = get_object_or_404(Post.objects.select_related('author'), id=id)
    serializer = PostSerializer(instance=post)
    return Response(serializer.data)
