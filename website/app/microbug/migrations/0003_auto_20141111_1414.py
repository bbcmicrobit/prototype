# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microbug', '0002_remove_version_store_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created At')),
                ('version', models.ForeignKey(to='microbug.Version')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='version',
            name='name',
        ),
        migrations.AddField(
            model_name='version',
            name='lines_of_code_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='version',
            name='previous_version',
            field=models.ForeignKey(blank=True, to='microbug.Version', null=True),
            preserve_default=True,
        ),
    ]
