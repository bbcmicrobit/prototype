# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('microbug', '0004_tutorial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='program',
            name='owner',
            field=models.ForeignKey(default=None, blank=True, to='microbug.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='version',
            name='owner',
            field=models.ForeignKey(default=None, blank=True, to='microbug.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
