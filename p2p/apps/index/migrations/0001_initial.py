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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='文章标题', max_length=50)),
                ('desc', models.CharField(verbose_name='文章描述', max_length=100)),
                ('source', models.CharField(verbose_name='文章来源', max_length=50)),
                ('content', models.TextField(verbose_name='文章内容')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='是否推荐')),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-date_publish'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='分类名称', max_length=30)),
                ('index', models.IntegerField(default=999, verbose_name='分类的排序')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
                'ordering': ['index', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='标的种类', max_length=30)),
                ('index', models.IntegerField(default=999, verbose_name='分类排序')),
            ],
            options={
                'verbose_name': '标的种类',
                'verbose_name_plural': '标的种类',
                'ordering': ['index', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Invest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(default=0.0, verbose_name='投资金额', decimal_places=2, blank=True, max_digits=9)),
                ('date_publish', models.DateTimeField(verbose_name='投资时间', auto_now_add=True)),
                ('status', models.CharField(default=1, verbose_name='投资状态', max_length=2, choices=[('1', '成功'), ('0', '失败')])),
            ],
            options={
                'verbose_name': '投资记录',
                'verbose_name_plural': '投资记录',
                'ordering': ['-date_publish'],
            },
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='借款标题', max_length=100)),
                ('desc', models.CharField(verbose_name='借款基本描述', max_length=100)),
                ('content', models.TextField(verbose_name='借款详细内容')),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('term', models.CharField(verbose_name='投资期限', max_length=50)),
                ('repayment', models.CharField(default=0, verbose_name='还款期限', max_length=50)),
                ('price', models.DecimalField(default=0.0, verbose_name='总额', decimal_places=2, blank=True, max_digits=9)),
                ('incomemode', models.CharField(verbose_name='收益方式', max_length=50)),
                ('status', models.BooleanField(default=False, verbose_name='审核状态')),
                ('created_at', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('classify', models.ForeignKey(null=True, to='index.Classify', verbose_name='标的种类', blank=True)),
                ('user', models.ForeignKey(verbose_name='发标用户', to='home.User')),
            ],
            options={
                'verbose_name': '标的信息',
                'verbose_name_plural': '标的信息',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='invest',
            name='trade',
            field=models.ForeignKey(verbose_name='投资项目', to='index.Trade'),
        ),
        migrations.AddField(
            model_name='invest',
            name='user',
            field=models.ForeignKey(verbose_name='投资用户', to='home.User'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, to='index.Category', verbose_name='分类', blank=True),
        ),
    ]
