# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import microbug.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilitatorRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_pending', models.BooleanField(default=True)),
                ('was_accepted', models.NullBooleanField(default=None)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('resolved_at', models.DateTimeField(default=None, null=True, blank=True)),
                ('child', models.ForeignKey(related_name=b'requests_by', to=settings.AUTH_USER_MODEL)),
                ('facilitator', models.ForeignKey(related_name=b'requests_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('edit_phrase', models.CharField(default=microbug.models.default_edit_phrase, max_length=200)),
                ('description', models.TextField(default=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created At')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('realname', models.CharField(max_length=200, null=True, blank=True)),
                ('question_1', models.CharField(max_length=200, null=True, blank=True)),
                ('question_2', models.CharField(max_length=200, null=True, blank=True)),
                ('question_3', models.CharField(max_length=200, null=True, blank=True)),
                ('question_4', models.CharField(max_length=200, null=True, blank=True)),
                ('question_5', models.CharField(max_length=200, null=True, blank=True)),
                ('question_6', models.CharField(max_length=200, null=True, blank=True)),
                ('question_7', models.CharField(max_length=200, null=True, blank=True)),
                ('question_8', models.CharField(max_length=200, null=True, blank=True)),
                ('question_9', models.CharField(max_length=200, null=True, blank=True)),
                ('question_10', models.CharField(max_length=200, null=True, blank=True)),
                ('facilitators', models.ManyToManyField(related_name=b'children', to='microbug.UserProfile')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_uuid', models.CharField(max_length=64)),
                ('lines_of_code_count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created At')),
                ('owner', models.ForeignKey(default=None, blank=True, to='microbug.UserProfile', null=True)),
                ('previous_version', models.ForeignKey(blank=True, to='microbug.Version', null=True)),
                ('program', models.ForeignKey(related_name=b'+', to='microbug.Program', null=True)),
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
            model_name='program',
            name='version',
            field=models.ForeignKey(related_name=b'+', to='microbug.Version'),
            preserve_default=True,
        ),
    ]
