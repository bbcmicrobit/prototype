# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microbug', '0005_auto_20141126_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='program',
            field=models.ForeignKey(related_name=b'+', to='microbug.Program', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='program',
            name='version',
            field=models.ForeignKey(related_name=b'+', to='microbug.Version'),
        ),
    ]
