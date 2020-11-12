from django.contrib import admin

from .models import Post, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'slug')
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'body', 'slug')


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'slug')
 

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
