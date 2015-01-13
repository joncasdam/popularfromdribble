# -*- encoding: utf-8 -*-
#
from django.db import models


class Player(models.Model):
    name = models.CharField(u'Nome', null=True, blank=False, max_length=250)
    username = models.CharField(u'Username', null=True, blank=False, max_length=250)
    avatar_url = models.URLField(u'Avatar', null=True, blank=True)
    dribble_id = models.IntegerField(u'Id no Dribble', null=False, blank=False)
    location = models.CharField(u'Local', null=True, blank=True, max_length=250)
    created_at = models.DateTimeField(u'Data criação', null=True, blank=False)
    website_url = models.URLField(u'Url pessoal', null=True, blank=True)
    twitter_username = models.CharField(u'Usuário twitter', null=True, blank=True, max_length=250)
    drafted_by_player_id = models.IntegerField(u'por quem foi draftado', null=True, blank=True)
    likes_count = models.IntegerField(u'Likes dados', null=True, blank=True)
    likes_received_count = models.IntegerField(u'Likes recebidos', null=True, blank=True)
    comments_count = models.IntegerField(u'Comentários feitos', null=True, blank=True)
    comments_received_count = models.IntegerField(u'Comentários recebidos', null=True, blank=True)
    followers_count = models.IntegerField(u'Seguidores', null=True, blank=True)
    following_count = models.IntegerField(u'Seguindo', null=True, blank=True)
    rebounds_count = models.IntegerField(u'Rebounds feitos', null=True, blank=True)
    rebounds_received_count = models.IntegerField(u'Rebounds recebidos', null=True, blank=True)
    draftees_count = models.IntegerField(u'Número de draftees', null=True, blank=True)
    shots_count = models.IntegerField(u'Número de shots', null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.name


class Entrada(models.Model):
    title = models.CharField(u'Título', null=True, blank=True, max_length=250)
    description = models.TextField(u'Descrição', null=True, blank=True)
    views_count = models.IntegerField(u'Views', null=True, blank=True)
    url = models.URLField(u'Url', null=True, blank=False)
    short_url = models.CharField(u'Url curta', null=True, blank=True, max_length=250)
    created_at = models.DateTimeField(u'Data criação', null=True, blank=False)
    player = models.ForeignKey(Player, verbose_name='Player', related_name='entradas')
    likes_count = models.IntegerField(u'Likes', null=True, blank=True)
    comments_count = models.IntegerField(u'Comentários', null=True, blank=True)
    rebounds_count = models.IntegerField(u'Rebounds', null=True, blank=True)
    height = models.IntegerField(u'Altura (px)', null=True, blank=True)
    width = models.IntegerField(u'Largura (px)', null=True, blank=True)
    image_400_url = models.URLField(u'Imagem 400px')
    # 'rebound_source_id',
    image_url = models.URLField(u'Url imagem')
    image_teaser_url = models.URLField(u'Imagem teaser')
    dirbble_id = models.IntegerField(u'Id no dribble', null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.title
