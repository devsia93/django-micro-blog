from django.urls import path
from .views import *


urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('posts/<int:id_post>/', PostDetailView.as_view()),
    path('tags/', TagListView.as_view()),
    path('tags/<int:id_tag>/', TagDetailView.as_view()),
    path('tags/create/', TagCreateView.as_view()),
    path('comments/', CommentListView.as_view()),
    path('comments/<int:id_comment>/', CommentDetailView.as_view()),
    path('comments/<pk>/create', CommentCreateView.as_view()),
]
