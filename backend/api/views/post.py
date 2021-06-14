from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from api.serializers import PostSerializer
from blog.models import Post, Tag


class PostsOfTagView(ListAPIView):
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
