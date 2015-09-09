# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogspost_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='header',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('intro', models.CharField(max_length=150)),
            ],
        ),
    ]
