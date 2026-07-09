from django.contrib import admin
from .models import Category,Article,Tag
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(Article)
class ArticleAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'author','category','status')
    list_filter = ('status','category','created_at')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}

    def publish_articles(self, request, queryset):
        queryset.update(status='published')
    publish_articles.short_description = "Tanlanganllarni nashr et"


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display        = ('name',)

@admin.register(Tag)
class TagAdmin(TabbedTranslationAdmin):
    list_display        = ('name',)
