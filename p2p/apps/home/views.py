#coding:utf-8
import logging
import datetime
import socket
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from p2p.apps.home.forms import *
from p2p.apps.home.models import *
from django.core.mail import send_mail
from django.contrib.auth import logout, login
from django.contrib.auth.hashers import make_password
# Create your views here.
logger = logging.getLogger('blog.views')

def global_setting(request):
    username = request.COOKIES.get('username','')
    if username:
        login = 1
    else:
        login = 0
    return locals()

#注册
def regist(request):
    # if req.method == 'POST':
    #     uf = UserForm(req.POST)
    #     if uf.is_valid():
    #         #获得表单数据
    #         username = uf.cleaned_data['username']
    #         password = uf.cleaned_data['password']
    #         #添加到数据库
    #         User.objects.create(username=username,password=password)
    #         return HttpResponse('regist success!!')
    # else:
    #     uf = UserForm()
    # return render_to_response('regist.html',{'uf':uf},context_instance=RequestContext(req))
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                # 注册
                user = User.objects.create(username=reg_form.cleaned_data["username"],
                                    email=reg_form.cleaned_data["email"],
                                    url=reg_form.cleaned_data["url"],
                                    password=reg_form.cleaned_data["password"],)
                user.save()

                # 登录
                # user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                # login(request, user)
                response = HttpResponseRedirect('source_url')
                # #将username写入浏览器的cookie,失效时间为3600
                response.set_cookie('username',user.username,3600)
                # return redirect(request.POST.get('source_url'))
                return response
            else:
                return render(request, 'failure.html', {'reason': reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        logger.error(e)
    return render(request, 'regist.html', locals())

#登录
def login(request):
    # if req.method == 'POST':
    #     uf = UserForm(req.POST)
    #     if uf.is_valid():
    #         #获取表单数据
    #         username = uf.cleaned_data['username']
    #         password = uf.cleaned_data['password']
    #         #获取的表单数据与数据库进行比较
    #         user = User.objects.filter(username__exact = username,password__exact = password)
    #
    #         if user:
    #             #比较成功，跳转index
    #             response = HttpResponseRedirect('/home/index/')
    #             #将username写入浏览器的cookie,失效时间为3600
    #             response.set_cookie('username',username,3600)
    #             return response
    #         else:
    #             #比较失败
    #             return HttpResponseRedirect('/home/login/')
    # else:
    #     uf = UserForm()
    #
    # return render_to_response('login.html',{'uf':uf},context_instance = RequestContext(req))
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 登录
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = User.objects.get(username__exact = username,password__exact = password)
                # return render(request, 'failure.html', {'reason': user})
                if user:
                    response = HttpResponseRedirect('source_url')
                    # #将username写入浏览器的cookie,失效时间为3600
                    response.set_cookie('username',username,3600)
                    # return redirect(request.POST.get('source_url'))
                    # User.objects.filter(id=user.id).update(last_log_time=datetime.datetime.now())
                    user.last_log_time = datetime.datetime.now()
                    user.save()
                    user.last_log_ip = socket.gethostbyname(socket.gethostname())
                    user.save()
                    return response
                else:
                    return render(request, 'failure.html', {'reason': '登录验证失败'})
            else:
                return render(request, 'failure.html', {'reason': login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
    return render(request, 'login.html', locals())

def index(request):
    return render(request, 'login.html', locals())


#退出
def logout(request):
    response = HttpResponse(request.META['HTTP_REFERER'])
    #清理cookie里保存的username
    response.delete_cookie('username')
    return response
    # try:
    #     logout(request)
    # except Exception as e:
    #     print(e)
    #     logger.error(e)
    # return redirect(request.META['HTTP_REFERER'])

#发送邮件
def email(request):
    # if request.method == "POST":
#        方式一：
    email = send_mail('subject', 'this is the message of email', 'cecotw@163.com', ['249508741@qq.com','cecotw@126.com'], fail_silently=True)

#        方式二：
#         message1 = ('subject1','this is the message of email1','pythonsuper@gmail.com',['1565208411@qq.com','xinxinyu2011@163.com'])
#         message2 = ('subject2','this is the message of email2','pythonsuper@gmail.com',['1373763906@qq.com','xinxinyu2011@163.com'])
#         send_mass_mail((message1,message2), fail_silently=False)

#        方式三：防止邮件头注入
#         try:
#             send_mail(subject, message, from_email, recipient_list, fail_silently, auth_user, auth_password, connection)
#         except BadHeaderError:
#             return HttpResponse('Invaild header fount.')

#        方式四：EmailMessage()
        #首先实例化一个EmailMessage()对象
#         em = EmailMessage('subject','body','from@example.com',['1565208411@qq.com'],['xinxinyu2011@163.com'],header={'Reply-to':'another@example.com'})
        #调用相应的方法

#         方式五：发送多用途邮件
#         subject,form_email,to = 'hello','from@example.com','1565208411@qq.com'
#         text_content = 'This is an important message'
#         html_content = u'<b>激活链接：</b><a href="http://www.baidu.com">http:www.baidu.com</a>'
#         msg = EmailMultiAlternatives(subject,text_content,form_email,[to])
#         msg.attach_alternative(html_content, 'text/html')
#         msg.send()

#       发送邮件成功了给管理员发送一个反馈
#         mail_admins(u'用户注册反馈', u'当前XX用户注册了该网站', fail_silently=True)
    return HttpResponse(email)
#     return render_to_response('user/bonus.html')




















