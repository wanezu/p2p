# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('desc', models.CharField(max_length=100, verbose_name='文章描述')),
                ('source', models.CharField(max_length=50, verbose_name='文章来源')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='是否推荐')),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
                'ordering': ['-date_publish'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('index', models.IntegerField(default=999, verbose_name='分类的排序')),
            ],
            options={
                'verbose_name_plural': '文章分类',
                'verbose_name': '文章分类',
                'ordering': ['index', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30, verbose_name='标的种类')),
                ('index', models.IntegerField(default=999, verbose_name='分类排序')),
            ],
            options={
                'verbose_name_plural': '标的种类',
                'verbose_name': '标的种类',
                'ordering': ['index', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Invest',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, blank=True, verbose_name='投资金额')),
                ('date_publish', models.DateTimeField(verbose_name='投资时间', auto_now_add=True)),
                ('status', models.CharField(choices=[('1', '成功'), ('0', '失败')], default=1, max_length=2, verbose_name='投资状态')),
            ],
            options={
                'verbose_name_plural': '投资记录',
                'verbose_name': '投资记录',
                'ordering': ['-date_publish'],
            },
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='借款标题')),
                ('desc', models.CharField(max_length=100, verbose_name='借款基本描述')),
                ('content', models.TextField(verbose_name='借款详细内容')),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('term', models.CharField(max_length=50, verbose_name='投资期限')),
                ('repayment', models.CharField(default=0, max_length=50, verbose_name='还款期限')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, blank=True, verbose_name='总额')),
                ('incomemode', models.CharField(max_length=50, verbose_name='收益方式')),
                ('status', models.BooleanField(default=False, verbose_name='审核状态')),
                ('created_at', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('classify', models.ForeignKey(null=True, to='index.Classify', blank=True, verbose_name='标的种类')),
                ('user', models.ForeignKey(to='home.User', verbose_name='发标用户')),
            ],
            options={
                'verbose_name_plural': '标的信息',
                'verbose_name': '标的信息',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='invest',
            name='trade',
            field=models.ForeignKey(to='index.Trade', verbose_name='投资项目'),
        ),
        migrations.AddField(
            model_name='invest',
            name='user',
            field=models.ForeignKey(to='home.User', verbose_name='投资用户'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, to='index.Category', blank=True, verbose_name='分类'),
        ),
    ]
