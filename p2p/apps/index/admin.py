from django.contrib import admin
from p2p.apps.index.models import *
# Register your models here.
@admin.register(Classify)
class ClassifyAdmin(admin.ModelAdmin):
    list_display = ('name','index')
    list_per_page = 20
    search_fields = ['name']

@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('title','desc','created_at')
    list_per_page = 20
    ordering = ('created_at',)
    search_fields = ('title','created_at',)
    list_editable = ('desc',)

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

@admin.register(Invest)
class InvestAdmin(admin.ModelAdmin):
    list_display = ('user','trade','price','date_publish','status',)
    list_per_page = 20
    search_fields = ['user','trade']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc','source',)
    list_display_links = ('title', 'desc','source', )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

# admin.site.register(Article, ArticleAdmin)
# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','index')
    list_per_page = 20
    search_fields = ['name']