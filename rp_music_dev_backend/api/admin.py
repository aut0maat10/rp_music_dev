from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
from api.models import Post, Category
class MarkdownxModelAdmin(MarkdownxModelAdmin):
    list_display = ['id', 'title', 'body', 'blurb',
                  'owner', 'image', 'categories']

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Category)
# admin.site.register(PostAdmin)
