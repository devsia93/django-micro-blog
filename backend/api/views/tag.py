from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication

from api.serializers import TagSerializer
from blog.models import Tag


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = (TokenAuthentication,)
