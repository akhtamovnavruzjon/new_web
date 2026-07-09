from django.contrib import admin
from .models import Comment,Like

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','body','article','created_up')
    search_fields = ('author','created_up')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user','article')