from rest_framework import serializers
from ..models import *


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'text',
                  'date_pub', 'approved_comment', 'post')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'slug', 'title', 'body',
                  'tags', 'date_pub', 'comments')
        # extra_kwargs = {'tags': {'required': False},
        #                 'comments': {'required': False}}


class TagSerializer(serializers.ModelSerializer):
    # posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ('id', 'slug', 'title')
        # extra_kwargs = {'posts': {'required': False}}
