__author__ = 'root'

from django.conf.urls import patterns, url
from p2p.apps.index import views
from p2p.apps.index import user_views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^trade/$',views.trade,name = 'trade'),
    url(r'^trade_list$',views.trade_list,name = 'trade_list'),
    url(r'^notice$',views.notice,name = 'notice'),
    url(r'^notice_de$',views.notice_de,name = 'notice_de'),
    url(r'^media$',views.media,name = 'media'),
    url(r'^media_de$',views.media_de,name = 'media_de'),
    #个人中心install
    url(r'^member/$',user_views.member,name = 'member'),
    url(r'^install/$',user_views.install,name = 'install'),
    url(r'^load/$',user_views.load,name = 'load'),
    url(r'^EMCode$',user_views.EMCode,name = 'EMCode'),
]