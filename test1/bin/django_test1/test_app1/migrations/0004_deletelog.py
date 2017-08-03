# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app1', '0003_auto_20170712_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='deletelog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'permissions': (('\u68c0\u7d22', '\u68c0\u7d22\u6743\u9650'), ('\u65b0\u589e', '\u65b0\u589e\u6743\u9650'), ('\u5220\u9664', '\u5220\u9664\u6743\u9650'), ('\u4fee\u6539', '\u4fee\u6539\u6743\u9650'), ('\u6062\u590d', '\u6062\u590d\u6743\u9650')),
            },
        ),
    ]
