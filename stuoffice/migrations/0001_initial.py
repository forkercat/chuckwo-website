# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(default=b'', max_length=200, verbose_name='\u53cd\u9988\u5185\u5bb9')),
                ('date', models.DateTimeField(verbose_name='\u65e5\u671f')),
            ],
        ),
    ]
