from rest_framework.serializers import ModelSerializer

from blog.models import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'slug', 'title')
