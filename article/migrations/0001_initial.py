# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('content', models.CharField(max_length=10000, verbose_name=b'Content')),
                ('status', models.IntegerField(default=0, verbose_name=b'Status', choices=[(0, b'normal'), (-1, b'deleted'), (10, b'Selected')])),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('block', models.ForeignKey(verbose_name=b'Block', to='block.Block')),
                ('owner', models.ForeignKey(verbose_name=b'Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
        ),
    ]
