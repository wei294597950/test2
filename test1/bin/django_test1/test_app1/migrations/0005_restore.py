# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app1', '0004_deletelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='restore',
            fields=[
                ('date', models.DateTimeField()),
                ('user', models.CharField(max_length=50)),
                ('option', models.CharField(max_length=50)),
                ('qaid', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '\u6062\u590d',
                'verbose_name_plural': '\u6062\u590d',
            },
        ),
    ]
