# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20151122_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bank_number',
            field=models.CharField(max_length=100, default='', verbose_name='银行卡号'),
        ),
    ]
