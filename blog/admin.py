from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_time')
    search_fields = ('title', 'content')
    list_filter = ('created_time',)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_time')
    search_fields = ('content', 'user__username', 'post__title')
    list_filter = ('created_time',)
