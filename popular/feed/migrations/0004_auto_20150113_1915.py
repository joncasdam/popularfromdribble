# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20150113_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='image_400_url',
            field=models.ImageField(upload_to=b'entradas', null=True, verbose_name='Imagem 400'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='image_teaser_url',
            field=models.ImageField(upload_to=b'entradas', null=True, verbose_name='Imagem teaser'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='image_url',
            field=models.ImageField(upload_to=b'entradas', null=True, verbose_name='Url imagem'),
            preserve_default=True,
        ),
    ]
