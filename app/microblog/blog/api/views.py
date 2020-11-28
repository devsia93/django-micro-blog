from rest_framework import generics
from ..models import *
from .serializers import *
from .utils import *

class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(ObjectDetailMixin, generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    argument = 'id_tag'


class PostListView(generics.ListAPIView):
    # Базовый запрос, используемый для извлечения объектов.
    queryset = Post.objects.all()
    # Класс для сериализации объектов.
    serializer_class = PostSerializer


class PostDetailView(ObjectDetailMixin, generics.RetrieveAPIView, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    argument = 'id_post'


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(ObjectDetailMixin, generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    argument = 'id_comment'