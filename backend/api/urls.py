from django.urls import path
from .views import TagViewSet, PostViewSet, CommentViewSet, PostsOfTagView, CommentsOfPostView
from rest_framework import routers

project_router = routers.DefaultRouter()

project_router.register(r'tags', TagViewSet)
project_router.register(r'posts', PostViewSet)
project_router.register(r'comments', CommentViewSet)

urlpatterns = [
    *project_router.urls,
    path('tags/<int:pk>/posts/', PostsOfTagView.as_view()),
    path('posts/<int:pk>/comments/', CommentsOfPostView.as_view()),
]
