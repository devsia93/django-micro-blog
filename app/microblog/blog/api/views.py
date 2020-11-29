from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
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


class TagCreateView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, format=None):
        tag = Tag(title=request.data['title'], slug=request.data['slug'])
        serializer = TagSerializer(data=tag)
        if serializer.is_valid(raise_exception=True):
            tag_saved = serializer.save()
            return Response({'successfully':True})
        return Response({'successfully':False})


class PostListView(generics.ListAPIView):
    # Базовый запрос, используемый для извлечения объектов.
    queryset = Post.objects.all()
    # Класс для сериализации объектов.
    serializer_class = PostSerializer


class PostDetailView(ObjectDetailMixin, generics.RetrieveAPIView):
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


class CommentCreateView(APIView):

    def post(self, request, pk, format=None):
        post_blog = get_object_or_404(Post, pk=pk)
        comment = Comment(text=request.data['text'], author_name=request.data['author_name'], post=post_blog)
        post_blog.comments.add(comment, bulk=False)
        return Response({'successfully':True})
