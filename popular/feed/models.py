# -*- encoding: utf-8 -*-
from dateutil.parser import parse as date_parser
from imagekit.models import ImageSpecField
from pilkit.processors import Adjust, resize

from django.db import models

from .utils import download_image


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

    @classmethod
    def importa_player(cls, dados):
        player, c = cls.objects.get_or_create(username=dados['username'], dribble_id=dados['id'])
        if player:
            player.name = dados['name']
            player.avatar_url = dados['avatar_url']
            player.location = dados['location']
            player.created_at = date_parser(dados['created_at'])
            player.website_url = dados['website_url']
            player.twitter_username = dados['twitter_screen_name']
            player.drafted_by_player_id = dados['drafted_by_player_id']
            player.likes_count = dados['likes_count']
            player.likes_received_count = dados['likes_received_count']
            player.comments_count = dados['comments_count']
            player.comments_received_count = dados['comments_received_count']
            player.followers_count = dados['followers_count']
            player.following_count = dados['following_count']
            player.rebounds_count = dados['rebounds_count']
            player.rebounds_received_count = dados['rebounds_received_count']
            player.draftees_count = dados['draftees_count']
            player.shots_count = dados['shots_count']
            player.save()

        return player


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
    image_400_url = models.ImageField(u'Imagem 400', upload_to='entradas', null=True, blank=False)
    # 'rebound_source_id',
    image_url = models.ImageField(u'Url imagem', upload_to='entradas', null=True, blank=False)
    thumb_image = ImageSpecField([Adjust(contrast=1.1, sharpness=1.1), resize.ResizeToFill(800, 600)],
                                 source='image_url', format='PNG', options={'quality': 90})
    thumb_400 = ImageSpecField([Adjust(contrast=1.1, sharpness=1.1), resize.ResizeToFill(400, 300)],
                               source='image_url', format='PNG', options={'quality': 90})
    thumb_teaser = ImageSpecField([Adjust(contrast=1.1, sharpness=1.1), resize.ResizeToFill(200, 150)],
                                 source='image_url', format='PNG', options={'quality': 90})
    thumb_admin = ImageSpecField([Adjust(contrast=1.1, sharpness=1.1), resize.ResizeToFill(100, 75)],
                                 source='image_url', format='PNG', options={'quality': 90})
    image_teaser_url = models.ImageField(u'Imagem teaser', upload_to='entradas', null=True, blank=False)
    dribble_id = models.IntegerField(u'Id no dribble', null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.title

    @classmethod
    def importa_entrada(cls, dados, player):
        entrada, c = cls.objects.get_or_create(dribble_id=dados['id'], player=player)
        if entrada:
            entrada.title = dados['title']
            entrada.description = dados['description']
            entrada.views_count = dados['views_count']
            entrada.url = dados['url']
            entrada.short_url = dados['short_url']
            entrada.created_at = date_parser(dados['created_at'])
            entrada.likes_count = dados['likes_count']
            entrada.comments_count = dados['comments_count']
            entrada.rebounds_count = dados['rebounds_count']
            entrada.height = dados['height']
            entrada.width = dados['width']

            if dados.get('image_400_url', None):
                nome_400, arquivo_400 = download_image(dados['image_400_url'])
                if nome_400 and arquivo_400:
                    entrada.image_400_url.save(nome_400, arquivo_400)

            nome_teaser, arquivo_teaser = download_image(dados['image_teaser_url'])
            if nome_teaser and arquivo_teaser:
                entrada.image_teaser_url.save(nome_teaser, arquivo_teaser)

            nome_img, arquivo_img = download_image(dados['image_url'])
            if nome_img and arquivo_img:
                entrada.image_url.save(nome_img, arquivo_img)

            entrada.save()
        return entrada

    def to_dict(self):
        return {'id': self.id,
                'title': self.title,
                'description': self.description,
                'image_url': self.thumb_image.url if self.image_url else None,
                'autor': self.player.name,
                'avatar_autor': self.player.avatar_url,
                'views': self.views_count}
