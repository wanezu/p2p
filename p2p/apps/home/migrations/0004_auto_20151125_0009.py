# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_user_bank_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='invit_code',
            field=models.CharField(max_length=100, verbose_name='我的邀请码', default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='inviter',
            field=models.CharField(max_length=100, verbose_name='我的邀请人', default=''),
        ),
    ]
