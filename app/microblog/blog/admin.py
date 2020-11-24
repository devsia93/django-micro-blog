from django.contrib import admin

from .models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'slug')
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'body', 'slug')


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'slug')
 

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'text', 'post')
    list_display_links = ('author_name', 'post')
    search_fields = ('author_name', 'text')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
