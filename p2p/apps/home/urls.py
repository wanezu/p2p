__author__ = 'root'

from django.conf.urls import patterns, url
from p2p.apps.home import views


urlpatterns = [
    url(r'^$', views.login, name = 'login'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
    url(r'^email/$',views.email,name = 'email'),
]