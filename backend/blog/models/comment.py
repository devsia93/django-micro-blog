from django.db import models

from precise_bbcode.fields import BBCodeTextField

from blog.models import Post


class Comment(models.Model):
    author_name = models.CharField(max_length=15, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = BBCodeTextField()
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['is_approved', 'date_pub']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return str(self.text)


