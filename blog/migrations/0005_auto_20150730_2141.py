# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150730_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogspost',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
