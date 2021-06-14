from django.contrib import admin

from blog.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'slug')
