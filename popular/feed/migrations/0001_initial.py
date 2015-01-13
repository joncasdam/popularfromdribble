# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, null=True, verbose_name='Nome')),
                ('username', models.CharField(max_length=250, null=True, verbose_name='Username')),
                ('avatar_url', models.URLField(null=True, verbose_name='Avatar', blank=True)),
                ('dribble_id', models.IntegerField(verbose_name='Id no Dribble')),
                ('location', models.CharField(max_length=250, null=True, verbose_name='Local', blank=True)),
                ('created_at', models.DateTimeField(null=True, verbose_name='Data cria\xe7\xe3o')),
                ('website_url', models.URLField(null=True, verbose_name='Url pessoal', blank=True)),
                ('twitter_username', models.CharField(max_length=250, null=True, verbose_name='Usu\xe1rio twitter', blank=True)),
                ('drafted_by_player_id', models.IntegerField(null=True, verbose_name='por quem foi draftado', blank=True)),
                ('likes_count', models.IntegerField(null=True, verbose_name='Likes dados', blank=True)),
                ('likes_received_count', models.IntegerField(null=True, verbose_name='Likes recebidos', blank=True)),
                ('comments_count', models.IntegerField(null=True, verbose_name='Coment\xe1rios feitos', blank=True)),
                ('comments_received_count', models.IntegerField(null=True, verbose_name='Coment\xe1rios recebidos', blank=True)),
                ('followers_count', models.IntegerField(null=True, verbose_name='Seguidores', blank=True)),
                ('following_count', models.IntegerField(null=True, verbose_name='Seguindo', blank=True)),
                ('rebounds_count', models.IntegerField(null=True, verbose_name='Rebounds feitos', blank=True)),
                ('rebounds_received_count', models.IntegerField(null=True, verbose_name='Rebounds recebidos', blank=True)),
                ('draftees_count', models.IntegerField(null=True, verbose_name='N\xfamero de draftees', blank=True)),
                ('shots_count', models.IntegerField(null=True, verbose_name='N\xfamero de shots', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
