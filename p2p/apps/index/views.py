import logging
import time
from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,HttpResponseRedirect
from p2p.apps.index.models import *
from p2p.apps.home.models import *
from django.conf import settings
# Create your models here.

logger = logging.getLogger('p2p.apps.index.views')

# def global_setting(request):


#显示首页
def index(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    trade_arr = Trade.objects.all()[:5]
    # return render(request, 'failure.html', {'reason': trade_arr})

    trade_arri = []
    for trade_ar in trade_arr:
        trade_arri.append(trade_ar)
        for item in trade_arri:
            trade_arrl = []
            if not hasattr(item, 'children_comment'):
                setattr(item, 'children_comment', [])
                # created_at =int(time.time() - time.mktime(trade_ar.created_at.timetuple()))
                # time_d = int(trade_ar.term) * 24 * 3600
                # time_diffl = time_d - created_at
                # time_finsh = time_handle(request, time_diffl)
                # trade_arrl.append(time_finsh)

                #获取投资详细信息
                invest_list = Invest.objects.filter(status=1,trade_id=trade_ar.id)
                #活取目前投资总金额
                invest_am = 0
                for invest in invest_list:
                    invest_am = invest_am + invest.price
                trade_arrl.append(invest_am)

                #获取剩余投资金额
                surplus = trade_ar.price - invest_am
                trade_arrl.append(surplus)
                trade_arrl.append(trade_ar.price)
                item.children_comment.append(trade_arrl)
                # print(trade_arrl)
    return render_to_response('index.html',locals())

#交易列表
def trade(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0

    trade_list = Trade.objects.all()
    trade_arr = getPage(request, trade_list)
    trade_arri = []
    for trade_ar in trade_arr:
        trade_arri.append(trade_ar)
        for item in trade_arri:
            trade_arrl = []
            if not hasattr(item, 'children_comment'):
                setattr(item, 'children_comment', [])

                #获取投资详细信息
                invest_list = Invest.objects.filter(status=1,trade_id=trade_ar.id)
                #活取目前投资总金额
                invest_am = 0
                for invest in invest_list:
                    invest_am = invest_am + invest.price
                trade_arrl.append(invest_am)

                #获取剩余投资金额
                surplus = trade_ar.price - invest_am
                trade_arrl.append(surplus)
                trade_arrl.append(trade_ar.price)
                item.children_comment.append(trade_arrl)
                # print(trade_arrl)
    return render_to_response('trade.html',locals())

# 分页代码
def getPage(request, trade_list):
    paginator = Paginator(trade_list, 1)
    try:
        page = int(request.GET.get('page', 1))
        trade_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        trade_list = paginator.page(1)
    return trade_list


# 标的详情
def trade_list(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0

    id = request.GET.get('id', None)
    trade_details = Trade.objects.get(id=id)
    created_at =int(time.time() - time.mktime(trade_details.created_at.timetuple()))
    time_d = int(trade_details.term) * 24 * 3600
    time_diffl = time_d - created_at
    time_finsh = time_handle(request, time_diffl)

    #获取投资详细信息
    invest_list = Invest.objects.filter(status=1,trade_id=id)
    #活取目前投资总金额
    invest_am = 0
    for invest in invest_list:
        invest_am = invest_am + invest.price

    #获取剩余投资金额
    surplus = trade_details.price - invest_am

    #投资进度
    speed = (invest_am / trade_details.price) * 100
    return render_to_response('trade_list.html',locals())

# 文章分页代码
def getPagen(request, trade_list):
    paginator = Paginator(trade_list, 10)
    try:
        page = int(request.GET.get('page', 1))
        trade_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        trade_list = paginator.page(1)
    return trade_list

#媒体报道
def media(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    notice_list = Article.objects.filter(category_id=1)
    notice_list = getPagen(request, notice_list)
    return render_to_response('media.html',locals())

#媒体报道详情
def media_de(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    id = request.GET.get('id', None)
    acticle_details = Article.objects.get(id=id)
    return render_to_response('media_de.html',locals())

#平台公告
def notice(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    notice_list = Article.objects.filter(category_id=2)
    notice_list = getPagen(request, notice_list)
    return render_to_response('notice.html',locals())



#媒体报道详情
def notice_de(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    id = request.GET.get('id', None)
    acticle_details = Article.objects.get(id=id)
    return render_to_response('notice_de.html',locals())

# 时间处理函数
def time_handle(request,time_diffl):
    if int(time_diffl / (12 * 30 * 24 * 3600)):
        time_diffy = int(time_diffl / (12 * 30 * 24 * 3600))
        time_diffy_t = time_diffl - int(time_diffl / (12 * 30 * 24 * 3600)) * 12 * 30 * 24 * 3600
        if int(time_diffy_t / (30 * 24 * 3600)):
            time_diffm = int(time_diffy_t / (30 * 24 * 3600))
            time_diffm_t = time_diffy_t - int(time_diffy_t / (30 * 24 * 3600)) * 30 * 24 * 3600
            if int(time_diffm_t / 24 * 3600):
                time_diffd = int(time_diffm_t / (24 * 3600))
                time_diffd_t = time_diffm_t - int(time_diffm_t / (24 * 3600)) * 24 * 3600
                if int(time_diffd_t / 3600):
                    time_diffh = int(time_diffd_t / 3600)
                    time_diffh_t = time_diffd_t - int(time_diffd_t / 3600) * 3600
                    if int(time_diffh_t / 60):
                        time_diffi = int(time_diffh_t / 60)
                        time_diffi_t = time_diffh_t - int(time_diffh_t / 60) * 60
                        time_finsh = str(time_diffy) + '年' + str(time_diffm) + '月' + str(time_diffd) + '天' + str(time_diffh) + '时' + str(time_diffi) + '分' + str(time_diffi_t) + '秒'
                    else:
                        time_finsh = str(time_diffy) + '年' + str(time_diffm) + '月' + str(time_diffd) + '天' + str(time_diffh) + '时' + '0分' + str(time_diffh_t) + '秒'
                else:
                    if int(time_diffd_t / 60):
                        time_diffi = int(time_diffd_t / 60)
                        time_diffi_t = time_diffd_t - int(time_diffd_t / 60) * 60
                        time_finsh = str(time_diffy) + '年' + str(time_diffm) + '月' + str(time_diffd) + '天' + '0时' + str(time_diffi) + '分' + str(time_diffi_t) + '秒'
                    else:
                        time_finsh = str(time_diffy) + '年' + str(time_diffm) + '月' + str(time_diffd) + '天' + '0时' + '0分' + str(time_diffd_t) + '秒'
            else:
                if int(time_diffm_t / 3600):
                    time_diffh = int(time_diffm_t / 3600)
                    time_diffh_t = time_diffm_t - int(time_diffm_t / 3600) * 3600
                    if int(time_diffh_t / 60):
                        time_diffi = int(time_diffh_t / 60)
                        time_diffi_t = time_diffh_t - int(time_diffh_t / 60) * 60
                        time_finsh = str(time_diffy) + '年' + str(time_diffm) + '月' + '0天' + str(time_diffh) + '时' + str(time_diffi) + '分' + str(time_diffi_t) + '秒'
                    else:
                        time_finsh = str(time_diffy) + '年' + str(time_diffm) + '月' + '0天' + str(time_diffh) + '时' + '0分' + str(time_diffh_t) + '秒'
                else:
                    if int(time_diffm_t / 60):
                        time_diffi = int(time_diffm_t / 60)
                        time_diffi_t = time_diffm_t - int(time_diffm_t / 60) * 60
                        time_finsh = str(time_diffy) + '年' + str(time_diffm) + '月' + '0天' + '0时' + str(time_diffi) + '分' + str(time_diffi_t) + '秒'
                    else:
                        time_finsh = str(time_diffy) + '年' + str(time_diffm) + '月' + '0天' + '0时' + '0分' + str(time_diffm_t) + '秒'
    else:
        if int(time_diffl / (30 * 24 * 3600)):
            time_diffm = int(time_diffl / (30 * 24 * 3600))
            time_diffm_t = time_diffl - int(time_diffl / (30 * 24 * 3600)) * 30 * 24 * 3600
            if int(time_diffm_t / 24 * 3600):
                time_diffd = int(time_diffm_t / (24 * 3600))
                time_diffd_t = time_diffm_t - int(time_diffm_t / (24 * 3600)) * 24 * 3600
                if int(time_diffd_t / 3600):
                    time_diffh = int(time_diffd_t / 3600)
                    time_diffh_t = time_diffd_t - int(time_diffd_t / 3600) * 3600
                    if int(time_diffh_t / 60):
                        time_diffi = int(time_diffh_t / 60)
                        time_diffi_t = time_diffh_t - int(time_diffh_t / 60) * 60
                        time_finsh = str(time_diffm) + '月' + str(time_diffd) + '天' + str(time_diffh) + '时' + str(time_diffi) + '分' + str(time_diffi_t) + '秒'
                    else:
                        time_finsh = str(time_diffm) + '月' + str(time_diffd) + '天' + str(time_diffh) + '时' + '0分' + str(time_diffh_t) + '秒'
                else:
                    if int(time_diffd_t / 60):
                        time_diffi = int(time_diffd_t / 60)
                        time_diffi_t = time_diffd_t - int(time_diffd_t / 60) * 60
                        time_finsh = str(time_diffm) + '月' + str(time_diffd) + '天' + '0时' + str(time_diffi) + '分' + str(time_diffi_t) + '秒'
                    else:
                        time_finsh = str(time_diffm) + '月' + str(time_diffd) + '天' + '0时' + '0分' + str(time_diffd_t) + '秒'
            else:
                if int(time_diffm_t / 3600):
                    time_diffh = int(time_diffm_t / 3600)
                    time_diffh_t = time_diffm_t - int(time_diffm_t / 3600) * 3600
                    if int(time_diffh_t / 60):
                        time_diffi = int(time_diffl / 60)
                        time_diffi_t = time_diffh_t - int(time_diffh_t / 60) * 60
                        time_finsh = str(time_diffm) + '月' + '0天' + str(time_diffh) + '时' + str(time_diffi) + '分' + str(time_diffi_t) + '秒'
                    else:
                        time_finsh = str(time_diffm) + '月' + '0天' + str(time_diffh) + '时' + '0分' + str(time_diffh_t) + '秒'
                else:
                    if int(time_diffm_t / 60):
                        time_diffi = int(time_diffm_t / 60)
                        time_diffi_t = time_diffm_t - int(time_diffm_t / 60) * 60
                        time_finsh = str(time_diffm) + '月' + '0天' + '0时' + str(time_diffi) + '分' + str(time_diffi_t) + '秒'
                    else:
                        time_finsh = str(time_diffm) + '月' + '0天' + '0时' + '0分' + str(time_diffm_t) + '秒'
        else:
            if int(time_diffl / (24 * 3600)):
                time_diffd = int(time_diffl / (24 * 3600))
                time_diffd_t = time_diffl - int(time_diffl / (24 * 3600)) * 24 * 3600
                if int(time_diffd_t / 3600):
                    time_diffh = int(time_diffd_t / 3600)
                    time_diffh_t = time_diffd_t - int(time_diffd_t / 3600) * 3600
                    if int(time_diffh_t / 60):
                        time_diffi = int(time_diffh_t / 60)
                        time_diffi_t = time_diffh_t - int(time_diffh_t / 60) * 60
                        time_finsh = str(time_diffd) + '天' + str(time_diffh) + '时' + str(time_diffi) + '分' + str(time_diffi_t) + '秒'
                    else:
                        time_finsh = str(time_diffd) + '天' + str(time_diffh) + '时' + '0分' + str(time_diffh_t) + '秒'
                else:
                    if int(time_diffd_t / 60):
                        time_diffi = int(time_diffd_t / 60)
                        time_diffi_t = time_diffd_t - int(time_diffd_t / 60) * 60
                        time_finsh = str(time_diffd) + '天' + '0时' + str(time_diffi) + '分' + str(time_diffi_t) + '秒'
                    else:
                        time_finsh = str(time_diffd) + '天' + '0时' + '0分' + str(time_diffd_t) + '秒'
            else:
                if int(time_diffl / 3600):
                    time_diffh = int(time_diffl / 3600)
                    time_diffh_t = time_diffl - int(time_diffl / 3600) * 3600
                    if int(time_diffh_t / 60):
                        time_diffi = int(time_diffl / 60)
                        time_diffi_t = time_diffh_t - int(time_diffh_t / 60) * 60
                        time_finsh = str(time_diffh) + '时' + str(time_diffi) + '分' + str(time_diffi_t) + '秒'
                    else:
                        time_finsh = str(time_diffh) + '时' + '0分' + str(time_diffh_t) + '秒'
                else:
                    if int(time_diffl / 60):
                        time_diffi = int(time_diffl / 60)
                        time_diffi_t = time_diffl - int(time_diffl / 60) * 60
                        time_finsh = str(time_diffi) + '分' + str(time_diffi_t) + '秒'
                    else:
                        time_finsh = str(time_diffl) + '秒'
    return time_finsh