# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blogspost',
            name='timestamp',
            field=models.DateTimeField(verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='header',
            name='intro',
            field=models.CharField(max_length=150, verbose_name=b'Introduction'),
        ),
    ]
