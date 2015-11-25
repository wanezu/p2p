# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

# 用户模型.
# 第一种：采用的继承方式扩展用户信息（本系统采用）
# 扩展：关联的方式去扩展用户信息
class User(models.Model):
    # avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name='用户头像')
    # qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    # mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    # url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')
    username = models.CharField("用户名",max_length=50,blank=True,null=False)
    password = models.CharField("密码",max_length=50,blank=True,null=False)
    email = models.CharField("邮箱",max_length=50,blank=True,null=False)
    user_phone = models.CharField("手机号码",max_length=50,blank=True,null=False)
    url = models.CharField("路径",max_length=50,blank=True,null=False)
    real_name = models.CharField("真实姓名",max_length=15,blank=True,null=False)
    last_log_time = models.DateTimeField("最后登录时间",default='')
    last_log_ip = models.CharField("最后登录ip",max_length=18,default='')
    reg_time = models.DateTimeField("注册时间",default='')
    reg_ip = models.CharField("注册ip",max_length=18,default='')
    sex = models.CharField("性别", max_length=2, choices=(('1', '男'), ('0', '女'), ),default='')
    photo = models.ImageField("用户头像",upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True)
    card = models.CharField("身份证号",max_length=20,default='')
    province = models.IntegerField("省",default=0)
    city = models.IntegerField("城市",default=0)
    region = models.IntegerField("地区",default=0)
    address_in = models.CharField("住址",max_length=100,default='')
    is_ban = models.CharField("是否禁止",max_length=2, choices=(('1', '是'), ('0', '否'), ),default=0)
    bank_number = models.CharField("银行卡号",max_length=100,default='')
    inviter = models.CharField("我的邀请人",max_length=100,default='')
    invit_code = models.CharField("我的邀请码",max_length=100,default='')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username
