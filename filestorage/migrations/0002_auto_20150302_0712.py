# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filestorage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(upload_to='/var/www/test.local/enmash_django.corp/enmashcorp/uploads/filestorage', max_length=500),
            preserve_default=True,
        ),
    ]
