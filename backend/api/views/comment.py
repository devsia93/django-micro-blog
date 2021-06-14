from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.serializers import CommentSerializer
from blog.models import Comment, Post


class CommentsOfPostView(ListAPIView):
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
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]
