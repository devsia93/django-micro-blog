from rest_framework.serializers import ModelSerializer

from blog.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'text',
                  'date_pub', 'approved_comment', 'post')
