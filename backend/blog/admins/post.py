from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'slug')
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'body', 'slug')
