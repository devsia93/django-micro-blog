from django.contrib import admin

from blog.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'text', 'post')
    list_display_links = ('author_name', 'post')
    search_fields = ('author_name', 'text')
    list_filter = ('is_approved',)
