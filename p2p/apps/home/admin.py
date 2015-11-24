from django.contrib import admin
from p2p.apps.home.models import User
# from p2p.apps.index.models import Trade
# Register your models here.

# admin.site.register(Classify)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','url','user_phone','real_name')
    list_per_page = 50
    search_fields = ('username','email')


# @admin.register(Trade)
# class TradeAdmin(admin.ModelAdmin):
#     list_display = ('title','created_at')
#     list_per_page = 20
#     ordering = ['created_at']
#     search_fields = ['title','created_at']