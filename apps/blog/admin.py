from django.contrib import admin
from .models import Article, Tag, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', )


class TagAdmin(admin.ModelAdmin):
    list_display = ('tags', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)