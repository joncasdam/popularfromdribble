# -*- encoding: utf-8 -*-

from django.core.management.base import BaseCommand

from feed.models import Player, Entrada
from feed.utils import fetch_popular_from_dribble


class Command(BaseCommand):
    '''
    Carga inicial de posts
    '''
    args = ''
    help = 'Realiza carga inicial de posts'

    def handle(self, *args, **options):
        dados = fetch_popular_from_dribble()
        shots = dados['shots']
        for shot in shots:
            if shot.get('player', None):
                print shot['image_url']
                player = Player.importa_player(shot['player'])
                Entrada.importa_entrada(shot, player)
        self.stdout.write('------------ FIM -----------')