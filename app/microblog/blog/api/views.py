from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from ..models import *
from .serializers import *
from .utils import *


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = (TokenAuthentication,)


class PostsOfTagView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)


    def get(self, request, pk):
        posts = Post.objects.filter(tags=get_object_or_404(Tag, pk=pk))
        response_data = PostSerializer(posts, many=True)
        return Response(response_data.data)


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = (TokenAuthentication,)


class CommentsOfPostView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    

    def get(self, request, pk):
        comments = Comment.objects.filter(post=get_object_or_404(Post, pk=pk))
        response_data = CommentSerializer(comments, many=True)
        return Response(response_data.data)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):
        if self.action in ('list', 'create', 'retrieve'):
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]

    # def get_object(self):
    #     hash_id = self.kwargs.get(self.lookup_url_kwarg, None)
    #     if hash_id is not None:
    #         obj = get_object_or_404(Project, hash_id=hash_id)
    #         ok = self.check_object_permissions(self.request, obj)
    #         return obj
    #     else:
    #         return None

    # def retrieve(self, request, *args, **kwargs):
    #     instance = get_object_or_404(Tag, id=self.kwargs['id_tag'])
    #     serializer = TagSerializer(instance=instance)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     serializer = TagSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class TagListView(generics.ListAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


# class TagDetailView(ObjectDetailMixin, generics.RetrieveAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     argument = 'id_tag'


# class TagCreateView(APIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def post(self, request, format=None):
#         tag = Tag(title=request.data['title'], slug=request.data['slug'])
#         serializer = TagSerializer(data=tag)
#         if serializer.is_valid(raise_exception=True):
#             tag_saved = serializer.save()
#             return Response({'successfully':True})
#         return Response({'successfully':False})


# class PostListView(generics.ListAPIView):
#     # Базовый запрос, используемый для извлечения объектов.
#     queryset = Post.objects.all()
#     # Класс для сериализации объектов.
#     serializer_class = PostSerializer


# class CommentDetailView(generics.ListAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

#     def get(self, request, pk):
#         post = Post.objects.get(pk=self.kwargs.get('pk'))
#         comments = self.queryset.filter(post=post)
#         response_data = CommentSerializer(comments, many=True)
#         return Response({"comments":response_data.data})


# class CommentListView(generics.ListAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# class CommentDetailView(ObjectDetailMixin, generics.RetrieveAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     argument = 'id_comment'


# class CommentCreateView(APIView):

#     def post(self, request, pk, format=None):
#         post_blog = get_object_or_404(Post, pk=pk)
#         comment = Comment(text=request.data['text'], author_name=request.data['author_name'], post=post_blog)
#         post_blog.comments.add(comment, bulk=False)
#         return Response({'successfully':True})
