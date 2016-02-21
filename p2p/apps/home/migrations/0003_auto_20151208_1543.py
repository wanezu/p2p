# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_friendly'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friendly',
            options={'verbose_name': '友情链接或合作伙伴', 'verbose_name_plural': '友情链接或合作伙伴', 'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='friendly',
            name='type',
            field=models.CharField(verbose_name='添加类型', choices=[('1', '友情链接'), ('2', '合作伙伴')], max_length=2, default=1),
        ),
    ]
