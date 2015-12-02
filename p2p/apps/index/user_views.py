__author__ = 'root'
import logging
from django.http import JsonResponse
import time
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,HttpResponseRedirect
from p2p.apps.index.models import *
from p2p.apps.home.models import *
from p2p.apps.index.forms import *
from django.template import RequestContext
from django.conf import settings

logger = logging.getLogger('p2p.apps.index.views')

#个人账户总览
def member(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    user_list = User.objects.get(username__exact=username)
    # print(notice_list.username)
    invest_list = Invest.objects.filter(user_id=user_list.id)
    invest_am = 0
    for invest in invest_list:
        invest_am = invest_am + invest.price
    redpaper_list = Redpaper.objects.filter(user_id=user_list.id,status=3)
    not_use_price = 0
    for redpaper_not in redpaper_list:
        not_use_price = not_use_price + redpaper_not.price
    return render_to_response('user/member.html',locals())

#个人设置
def install(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    user_list = User.objects.get(username__exact=username)
    # for userinfo in user_list:
    province = Region.objects.get(id=user_list.province)
    city = Region.objects.get(id=user_list.city)
    region = Region.objects.get(id=user_list.region)
    # print(province)
    return render_to_response('user/install.html',locals())

#投资记录
def load(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0

    try:
        user_list = User.objects.get(username__exact=username)
        id = user_list.id
        if request.method == 'POST':
            load = LoadForm(request.POST)
            if load.is_valid():
                status = request.POST.get('status')
                date_start = load.cleaned_data["date_start"]
                date_end = load.cleaned_data["date_end"]
                if int(status) == 0:
                    invest_list = Invest.objects.filter(user_id=id)
                    trade_arr = getPage(request, invest_list)
                    invest_arr = []
                    for invest_ar in trade_arr:
                        invest_arr.append(invest_ar)
                        for item in invest_arr:
                            invest_arrl = []
                            if not hasattr(item,'children_comment'):
                                setattr(item,'children_comment',[])
                                #获取项目详情信息
                                trade_list = Trade.objects.get(id=invest_ar.trade_id)
                                invest_arr.append(trade_list.title)
                                #获取项目是否满标
                                trade_invest = Invest.objects.filter(status=1,trade_id=trade_list.id)
                                invest_am = 0
                                for trade in trade_invest:
                                    invest_am = invest_am + trade.price

                                #标的创建时间
                                create_time = int(time.mktime(trade_list.created_at.timetuple()))
                                #标的投资期限
                                time_d = int(trade_list.term) * 24 * 3600
                                #当前时间
                                time_now = time.time()
                                #标的还款期限
                                repayment_time = int(trade_list.repayment) * 24 * 3600

                                if ((trade_list.price - invest_am) == 0) and (time_now - create_time < time_d):
                                    invest_st = "满标"
                                elif (time_now - create_time < time_d):
                                    invest_st = "投标中"
                                elif (time_now - create_time >= time_d):
                                    invest_st = "回款中"
                                elif (time_now - repayment_time - time_d - create_time > 0):
                                    invest_st = "已回款"
                                invest_arr.append(invest_st)
                                item.children_comment.append(invest_arr)
                    # print(invest_arrl)
                elif int(status) == 1:
                    invest_list = Invest.objects.filter(user_id=id)
                    for invest in invest_list:
                        trade_list = Trade.objects.get(id=invest.trade_id)
                        #获取项目是否满标
                        trade_invest = Invest.objects.filter(status=1,trade_id=trade_list.id)
                        invest_am = 0
                        for trade in trade_invest:
                            invest_am = invest_am + trade.price

                        #标的创建时间
                        create_time = int(time.mktime(trade_list.created_at.timetuple()))
                        #标的投资期限
                        time_d = int(trade_list.term) * 24 * 3600
                        #当前时间
                        time_now = time.time()
                        #标的还款期限
                        repayment_time = int(trade_list.repayment) * 24 * 3600
                        trade_arri = []
                        if ((trade_list.price - invest_am) < 0) and (time_now - create_time < time_d):
                            for item in trade_arri:
                                trade_arrl = []
                                if not hasattr(item, 'children_comment'):
                                    setattr(item, 'children_comment', [])
                                    trade_arrl.append(invest)
                                    item.children_comment.append(trade_arrl)
                    trade_arr = getPage(request, trade_arrl)
                elif int(status) == 2:
                    pass
                elif int(status) == 4:
                    pass
                elif int(status) == 5:
                    pass
                # print(date_end)
                # User.objects.filter(id=user_list.id).update(password=new_user_phone)
                # response = HttpResponseRedirect('source_url')
                # return response
            else:
                return render(request, 'failure.html', {'reason': LoadForm.errors})
        else:
            load = LoadForm(request.POST)
            invest_list = Invest.objects.filter(user_id=id)
            trade_arr = getPage(request, invest_list)
            print(trade_arr)
            invest_arr = []
            for invest_ar in trade_arr:
                invest_arr.append(invest_ar)
                for item in invest_arr:
                    invest_arrl = []
                    if not hasattr(item,'children_comment'):
                        setattr(item,'children_comment',[])
                        #获取项目详情信息
                        trade_list = Trade.objects.get(id=invest_ar.trade_id)
                        invest_arr.append(trade_list.title)
                        #获取项目是否满标
                        trade_invest = Invest.objects.filter(status=1,trade_id=trade_list.id)
                        invest_am = 0
                        for trade in trade_invest:
                            invest_am = invest_am + trade.price

                        #标的创建时间
                        create_time = int(time.mktime(trade_list.created_at.timetuple()))
                        #标的投资期限
                        time_d = int(trade_list.term) * 24 * 3600
                        #当前时间
                        time_now = time.time()
                        #标的还款期限
                        repayment_time = int(trade_list.repayment) * 24 * 3600

                        if ((trade_list.price - invest_am) == 0) and (time_now - create_time < time_d):
                            invest_st = "满标"
                        elif (time_now - create_time < time_d):
                            invest_st = "投标中"
                        elif (time_now - create_time >= time_d):
                            invest_st = "回款中"
                        elif (time_now - repayment_time - time_d - create_time > 0):
                            invest_st = "已回款"
                        invest_arr.append(invest_st)
                        # print(invest_arr)
                        item.children_comment.append(invest_arr)
    except Exception as e:
        logger.error(e)
    return render(request, 'user/load.html', locals())

#邮箱认证
def EMCode(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0

    # return login
    return render_to_response('user/load.html',locals())

#修改密码
def changepw(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    try:
        user_list = User.objects.get(username__exact=username)
        password = user_list.password
        if request.method == 'POST':
            changepwd = ChangepwForm(request.POST)
            if changepwd.is_valid():
                #修改密码
                new_password = changepwd.cleaned_data["new_password"]
                old_password = changepwd.cleaned_data["old_password"]
                if password == old_password:
                    User.objects.filter(id=user_list.id).update(password=new_password)
                    response = HttpResponseRedirect('source_url')
                    return response
                else:
                    response = HttpResponseRedirect('source_url')
                    return render(request, 'failure.html', {'reason': "您的旧密码有误！请重新输入！"})
            else:
                return render(request, 'failure.html', {'reason': ChangepwForm.errors})
        else:
            changepwd = ChangepwForm()
    except Exception as e:
        logger.error(e)
    # return render_to_response('user/changepw.html',locals())
    return render(request, 'user/changepw.html', locals())

#修改手机号码
def editmb(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    try:
        user_list = User.objects.get(username__exact=username)
        user_phone = user_list.user_phone
        if request.method == 'POST':
            phone = ChangephoneForm(request.POST)
            if phone.is_valid():
                #修改手机号码
                code = phone.cleaned_data["code"]
                # User.objects.filter(id=user_list.id).update(password=new_user_phone)
                response = HttpResponseRedirect('source_url')
                return response
            else:
                return render(request, 'failure.html', {'reason': ChangephoneForm.errors})
        else:
            phone = ChangephoneForm()
    except Exception as e:
        logger.error(e)
    return render(request, 'user/editmb.html', locals())

#用户充值
def charge(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    return render(request, 'user/charge.html', locals())


#用户提现
def cash(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    return render(request, 'user/cash.html', locals())

#资金记录
def money(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0

    try:
        user_list = User.objects.get(username__exact=username)
        id = user_list.id
        if request.method == 'POST':
            search = SearchForm(request.POST)
            if search.is_valid():
                log_info = request.POST.get("log_info")
                start = search.cleaned_data["start"]
                end = search.cleaned_data["end"]

                if log_info == '':
                    pass
                elif log_info == u'投资放款':
                    trade_arr = Invest.objects.filter(user_id=id)
                    # trade_arr = getPage(request, invest_list)
                    invest_arr = []
                    for invest_ar in trade_arr:
                        # print(invest_ar.trade_id)
                        invest_arr.append(invest_ar)
                        for item in invest_arr:
                            invest_arrl = []
                            if not hasattr(item,'children_comment'):
                                setattr(item,'children_comment',[])
                                #获取项目详情信息
                                trade_list = Trade.objects.get(id=invest_ar.trade_id)
                                invest_arrl.append(trade_list.title)
                                #获取项目是否满标
                                trade_invest = Invest.objects.filter(status=1,trade_id=trade_list.id)
                                invest_am = 0
                                for trade in trade_invest:
                                    invest_am = invest_am + trade.price

                                #标的创建时间
                                create_time = int(time.mktime(trade_list.created_at.timetuple()))
                                #标的投资期限
                                time_d = int(trade_list.term) * 24 * 3600
                                #当前时间
                                time_now = time.time()
                                #标的还款期限
                                repayment_time = int(trade_list.repayment) * 24 * 3600
                                invest_st = "投标中"
                                if ((trade_list.price - invest_am) == 0) and (time_now - create_time < time_d):
                                    invest_st = "满标"
                                elif (time_now - create_time < time_d):
                                    invest_st = "投标中"
                                elif (time_now - create_time >= time_d):
                                    invest_st = "回款中"
                                elif (time_now - repayment_time - time_d - create_time > 0):
                                    invest_st = "已回款"
                                invest_arrl.append(invest_st)
                                print(invest_arrl)
                                item.children_comment.append(invest_arrl)
            else:
                return render(request, 'failure.html', {'reason': SearchForm.errors})
        else:
            search = SearchForm()
    except Exception as e:
        logger.error(e)
    # print(trade_arr)
    return render(request, 'user/money.html', locals())


#回款计划
def loan(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    return render(request, 'user/loan.html', locals())


#还款计划
def refund(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    return render(request, 'user/refund.html', locals())

#合同列表
def contract(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    return render(request, 'user/contract.html', locals())

#邀请返利
def coupon(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    return render(request, 'user/coupon.html', locals())

#平台红包
def bonus(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    try:
        user_list = User.objects.get(username__exact=username)
        redpaper_list = Redpaper.objects.filter(user_id=user_list.id,status=3)
        not_use_price = 0
        for redpaper_not in redpaper_list:
            not_use_price = not_use_price + redpaper_not.price
        has_use_list = Redpaper.objects.filter(user_id=user_list.id,status=1)
        has_use = 0
        for redpaper_use in has_use_list:
            has_use = has_use + redpaper_use.price
        lose_list = Redpaper.objects.filter(user_id=user_list.id,status=2)
        lose_use = 0
        for redpaper_lose in lose_list:
            lose_use = lose_use + redpaper_lose.price
    except Exception as e:
        logger.error(e)
    return render(request, 'user/bonus.html', locals())

#平台红包
def setmessage(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    return render(request, 'user/setmessage.html', locals())

# 分页代码
def getPage(request, trade_list):
    paginator = Paginator(trade_list, 1)
    try:
        page = int(request.GET.get('page', 1))
        trade_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        trade_list = paginator.page(1)
    return trade_list