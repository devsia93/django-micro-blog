from rest_framework import serializers
from ..models import *


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('title','slug', 'id')


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('author_name', 'text', 'date_pub', 'post', 'id')
