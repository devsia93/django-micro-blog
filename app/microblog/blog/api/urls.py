from django.urls import path
from .views import *


urlpatterns = [
    path('posts', PostListView.as_view(), name='posts_list_url'),
    path('posts/<int:id_post>/', PostDetailView.as_view(), name='post_detail_url'),
    path('tags/', TagListView.as_view(), name='tags_list_url'),
    path('tags/<int:id_tag>/', TagDetailView.as_view(), name='tag_detail_url'),
    path('comments/', CommentListView.as_view(), name='comments_list_url'),
    path('comments/<int:id_comment>/', CommentDetailView.as_view(), name='comment_detail_url'),
]