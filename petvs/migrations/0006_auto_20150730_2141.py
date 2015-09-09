# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petvs', '0005_statistics_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='hot',
            field=models.IntegerField(default=0, verbose_name=b'Hot'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pic',
            field=models.CharField(max_length=200, verbose_name=b'Picture'),
        ),
    ]
