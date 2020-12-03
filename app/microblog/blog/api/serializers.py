from rest_framework import serializers
from ..models import *


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'slug', 'title')


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'slug', 'title', 'body', 'tags', 'date_pub')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author_name', 'text',
                  'date_pub', 'approved_comment')
