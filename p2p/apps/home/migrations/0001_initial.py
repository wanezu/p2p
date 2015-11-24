# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, verbose_name='用户名', max_length=50)),
                ('password', models.CharField(blank=True, verbose_name='密码', max_length=50)),
                ('email', models.CharField(blank=True, verbose_name='邮箱', max_length=50)),
                ('user_phone', models.IntegerField(verbose_name='手机号码', default=0)),
                ('url', models.CharField(blank=True, verbose_name='路径', max_length=50)),
                ('real_name', models.CharField(blank=True, verbose_name='真实姓名', max_length=15)),
                ('last_log_time', models.DateTimeField(verbose_name='最后登录时间', default='')),
                ('last_log_ip', models.CharField(verbose_name='最后登录ip', max_length=18, default='')),
                ('reg_time', models.DateTimeField(verbose_name='注册时间', default='')),
                ('reg_ip', models.CharField(verbose_name='注册ip', max_length=18, default='')),
                ('sex', models.CharField(max_length=2, verbose_name='性别', choices=[('1', '男'), ('0', '女')], default='')),
                ('photo', models.ImageField(blank=True, default='avatar/default.png', null=True, verbose_name='用户头像', upload_to='avatar/%Y/%m', max_length=200)),
                ('card', models.CharField(verbose_name='身份证号', max_length=20, default='')),
                ('province', models.IntegerField(verbose_name='省', default=0)),
                ('city', models.IntegerField(verbose_name='城市', default=0)),
                ('region', models.IntegerField(verbose_name='地区', default=0)),
                ('address_in', models.CharField(verbose_name='住址', max_length=100, default='')),
                ('is_ban', models.CharField(max_length=2, verbose_name='是否禁止', choices=[('1', '是'), ('0', '否')], default=0)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-id'],
            },
        ),
    ]
