# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Name')),
                ('desc', models.CharField(max_length=150, verbose_name=b'Description')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('manager', models.ForeignKey(verbose_name=b'author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'block',
                'verbose_name_plural': 'blocks',
            },
        ),
    ]
