# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logdelete',
            options={'verbose_name': '\u5220\u9664\u65e5\u5fd7', 'verbose_name_plural': '\u5220\u9664\u65e5\u5fd7'},
        ),
        migrations.AlterField(
            model_name='logdelete',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
