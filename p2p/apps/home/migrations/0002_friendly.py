# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendly',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='名称', default='', max_length=20)),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='连接添加时间')),
                ('photo', models.ImageField(null=True, blank=True, default='friendly/default.png', upload_to='friendly/%Y/%m', verbose_name='图片上传', max_length=200)),
                ('address', models.CharField(verbose_name='连接地址', default='', max_length=300)),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ['id'],
            },
        ),
    ]
