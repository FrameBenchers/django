from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'created_date')

admin.site.register(Blog, BlogAdmin)
