from django.contrib import admin
from post.models import Post, Category, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'create_at', 'update_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at', 'update_at']


@admin.register(Comment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at', 'update_at']
