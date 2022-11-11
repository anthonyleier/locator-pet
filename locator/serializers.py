from rest_framework import serializers
from django.contrib.auth.models import User


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=65)
    description = serializers.CharField(max_length=165)
    author = serializers.StringRelatedField()
