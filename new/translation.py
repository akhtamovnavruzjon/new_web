from modeltranslation.translator import register,TranslationOptions
from .models import Article,Category,Tag

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    field=('title','body')

@register(Category)
class ArticleTranslationOptions(TranslationOptions):
    field=('name',)

@register(Tag)
class ArticleTranslationOptions(TranslationOptions):
    field=('name',)

