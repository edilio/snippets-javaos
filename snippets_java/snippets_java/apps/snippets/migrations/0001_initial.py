# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100, blank=True)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
                ('language', models.CharField(default=b'python', max_length=100, choices=[(b'java', b'Java')])),
                ('style', models.CharField(default=b'friendly', max_length=100, choices=[(b'autumn', b'autumn'), (b'borland', b'borland'), (b'bw', b'bw'), (b'colorful', b'colorful'), (b'default', b'default'), (b'emacs', b'emacs'), (b'friendly', b'friendly'), (b'fruity', b'fruity'), (b'igor', b'igor'), (b'manni', b'manni'), (b'monokai', b'monokai'), (b'murphy', b'murphy'), (b'native', b'native'), (b'paraiso-dark', b'paraiso-dark'), (b'paraiso-light', b'paraiso-light'), (b'pastie', b'pastie'), (b'perldoc', b'perldoc'), (b'rrt', b'rrt'), (b'tango', b'tango'), (b'trac', b'trac'), (b'vim', b'vim'), (b'vs', b'vs'), (b'xcode', b'xcode')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_on',),
            },
        ),
    ]
