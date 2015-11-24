# -*- coding: utf-8 -*-
from django.db import models
from p2p.apps.home.models import User

#标的种类models
class Classify(models.Model):
    name = models.CharField(max_length=30,verbose_name='标的种类')
    index = models.IntegerField(default=999,verbose_name='分类排序')

    class Meta:
        verbose_name = '标的种类'
        verbose_name_plural = verbose_name
        ordering = ['index','id']

    def __str__(self):
        return self.name
#标的详情
class Trade(models.Model):
    user = models.ForeignKey(User,verbose_name='发标用户')
    title = models.CharField(max_length=100,verbose_name='借款标题')
    desc = models.CharField(max_length=100,verbose_name='借款基本描述')
    content = models.TextField(verbose_name='借款详细内容')
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    classify = models.ForeignKey(Classify,blank=True,null=True,verbose_name='标的种类')
    term = models.CharField(max_length=50,verbose_name='投资期限')
    price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,default=0.00,verbose_name='总额')
    incomemode = models.CharField(max_length=50,verbose_name='收益方式')
    status = models.BooleanField(default=False,verbose_name='审核状态')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        verbose_name = '标的信息'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']

    def __str__(self):
        return self.title
#投资记录
class Invest(models.Model):
    user = models.ForeignKey(User,verbose_name='投资用户')
    trade = models.ForeignKey(Trade,verbose_name='投资项目')
    price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,default=0.00,verbose_name='投资金额')
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name='投资时间')
    status = models.CharField(max_length=2, choices=(('1', '成功'), ('0', '失败'), ),default=1,verbose_name='投资状态')

    class Meta:
        verbose_name = '投资记录'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return self.status

# 分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=999,verbose_name='分类的排序')

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name

# 文章模型
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=100, verbose_name='文章描述')
    source = models.CharField(max_length=50, verbose_name='文章来源')
    content = models.TextField(verbose_name='文章内容')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return self.title