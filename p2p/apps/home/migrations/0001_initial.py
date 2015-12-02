# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Redpaper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('red_name', models.CharField(default='', verbose_name='红包名称', max_length=200)),
                ('get_time', models.DateTimeField(verbose_name='红包发放时间', auto_now_add=True)),
                ('con_time', models.DateTimeField(default='', verbose_name='红包消费时间')),
                ('deadline', models.DateTimeField(default='', verbose_name='红包过期时间')),
                ('price', models.DecimalField(default=0.0, verbose_name='红包金额', decimal_places=2, blank=True, max_digits=9)),
                ('status', models.CharField(default=3, verbose_name='红包状态', max_length=2, choices=[('1', '已提现'), ('2', '已失效'), ('3', '未使用')])),
                ('remarks', models.TextField(verbose_name='备注信息')),
            ],
            options={
                'verbose_name': '红包数据',
                'verbose_name_plural': '红包数据',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parent_id', models.IntegerField(default=0, verbose_name='父id')),
                ('region_name', models.CharField(default='', verbose_name='名称', max_length=50)),
                ('region_type', models.IntegerField(default=0, verbose_name='地区类型')),
                ('agency_id', models.IntegerField(default=0, verbose_name='代理')),
            ],
            options={
                'verbose_name': '城市列表',
                'verbose_name_plural': '城市列表',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(verbose_name='用户名', max_length=50, blank=True)),
                ('password', models.CharField(verbose_name='密码', max_length=50, blank=True)),
                ('email', models.CharField(verbose_name='邮箱', max_length=50, blank=True)),
                ('user_phone', models.CharField(verbose_name='手机号码', max_length=50, blank=True)),
                ('url', models.CharField(verbose_name='路径', max_length=50, blank=True)),
                ('real_name', models.CharField(verbose_name='真实姓名', max_length=15, blank=True)),
                ('last_log_time', models.DateTimeField(default='', verbose_name='最后登录时间')),
                ('last_log_ip', models.CharField(default='', verbose_name='最后登录ip', max_length=18)),
                ('reg_time', models.DateTimeField(default='', verbose_name='注册时间')),
                ('reg_ip', models.CharField(default='', verbose_name='注册ip', max_length=18)),
                ('sex', models.CharField(default='', verbose_name='性别', max_length=2, choices=[('1', '男'), ('0', '女')])),
                ('photo', models.ImageField(default='avatar/default.png', null=True, max_length=200, upload_to='avatar/%Y/%m', verbose_name='用户头像', blank=True)),
                ('card', models.CharField(default='', verbose_name='身份证号', max_length=20)),
                ('province', models.IntegerField(default=0, verbose_name='省')),
                ('city', models.IntegerField(default=0, verbose_name='城市')),
                ('region', models.IntegerField(default=0, verbose_name='地区')),
                ('address_in', models.CharField(default='', verbose_name='住址', max_length=100)),
                ('is_ban', models.CharField(default=0, verbose_name='是否禁止', max_length=2, choices=[('1', '是'), ('0', '否')])),
                ('bank_number', models.CharField(default='', verbose_name='银行卡号', max_length=100)),
                ('inviter', models.CharField(default='', verbose_name='我的邀请人', max_length=100)),
                ('invit_code', models.CharField(default='', verbose_name='我的邀请码', max_length=100)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='redpaper',
            name='user',
            field=models.ForeignKey(verbose_name='红包所属人', to='home.User'),
        ),
    ]
