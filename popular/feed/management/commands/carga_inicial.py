# -*- encoding: utf-8 -*-

import urllib2
import simplejson as json

from django.core.management.base import BaseCommand
from django.conf import settings

from feed.models import Player, Entrada


class Command(BaseCommand):
    '''
    Carga inicial de posts
    '''
    args = ''
    help = 'Realiza carga inicial de posts'

    def handle(self, *args, **options):
        req = urllib2.Request(settings.DRIBBLE_POPULAR_URL)
        resposta = urllib2.urlopen(req).read()
        dados = json.loads(resposta)
        shots = dados['shots']
        for shot in shots:
            if shot.get('player', None):
                print shot['image_url']
                player = Player.importa_player(shot['player'])
                entrada = Entrada.importa_entrada(shot, player)
        self.stdout.write('------------ FIM -----------')