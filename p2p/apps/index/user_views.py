__author__ = 'root'
import logging
import time
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,HttpResponseRedirect
from p2p.apps.index.models import *
from p2p.apps.home.models import *
from django.conf import settings

#个人账户总览
def member(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    user_list = User.objects.get(username__exact=username)
    # print(notice_list.username)
    return render_to_response('user/member.html',locals())

#个人设置
def install(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    user_list = User.objects.get(username__exact=username)
    return render_to_response('user/install.html',locals())

#投资记录
def load(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    return render_to_response('user/load.html',locals())

#邮箱认证
def EMCode(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0

    # return login
    return render_to_response('user/load.html',locals())