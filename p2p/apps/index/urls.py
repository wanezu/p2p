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
    url(r'^changepw/$',user_views.changepw,name = 'changepw'),
    url(r'^editmb/',user_views.editmb,name = 'editmb'),
    url(r'^EMCode$',user_views.EMCode,name = 'EMCode'),
    url(r'^charge/$',user_views.charge,name = 'charge'),
    url(r'^cash/$',user_views.cash,name = 'cash'),
    url(r'^money/$',user_views.money,name = 'money'),
    url(r'^loan/$',user_views.loan,name = 'loan'),
    url(r'^refund/$',user_views.refund,name = 'refund'),
    url(r'^contract/$',user_views.contract,name = 'contract'),
    url(r'^coupon/$',user_views.coupon,name = 'coupon'),
    url(r'^bonus/$',user_views.bonus,name = 'bonus'),
    url(r'^setmessage/$',user_views.setmessage,name = 'setmessage'),
]