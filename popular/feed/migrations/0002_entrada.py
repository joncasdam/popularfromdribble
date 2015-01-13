# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, null=True, verbose_name='T\xedtulo', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Descri\xe7\xe3o', blank=True)),
                ('views_count', models.IntegerField(null=True, verbose_name='Views', blank=True)),
                ('url', models.URLField(null=True, verbose_name='Url')),
                ('short_url', models.CharField(max_length=250, null=True, verbose_name='Url curta', blank=True)),
                ('created_at', models.DateTimeField(null=True, verbose_name='Data cria\xe7\xe3o')),
                ('likes_count', models.IntegerField(null=True, verbose_name='Likes', blank=True)),
                ('comments_count', models.IntegerField(null=True, verbose_name='Coment\xe1rios', blank=True)),
                ('rebounds_count', models.IntegerField(null=True, verbose_name='Rebounds', blank=True)),
                ('height', models.IntegerField(null=True, verbose_name='Altura (px)', blank=True)),
                ('width', models.IntegerField(null=True, verbose_name='Largura (px)', blank=True)),
                ('image_400_url', models.URLField(verbose_name='Imagem 400px')),
                ('image_url', models.URLField(verbose_name='Url imagem')),
                ('image_teaser_url', models.URLField(verbose_name='Imagem teaser')),
                ('dirbble_id', models.IntegerField(null=True, verbose_name='Id no dribble', blank=True)),
                ('player', models.ForeignKey(related_name='entradas', verbose_name=b'Player', to='feed.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
