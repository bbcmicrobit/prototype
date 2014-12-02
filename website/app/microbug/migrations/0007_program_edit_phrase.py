# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import microbug.models


class Migration(migrations.Migration):

    dependencies = [
        ('microbug', '0006_auto_20141128_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='edit_phrase',
            field=models.CharField(default=microbug.models.default_edit_phrase, max_length=200),
            preserve_default=True,
        ),
    ]
