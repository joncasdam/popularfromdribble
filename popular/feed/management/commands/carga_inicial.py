# -*- encoding: utf-8 -*-

from django.core.files import File
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    '''
    Carga inicial de posts
    '''
    args = ''
    help = 'Realiza carga inicial de posts'

    def handle(self, *args, **options):
        print 'oooooo!!!!!!ooooooo'
        self.stdout.write('oooooo!!!!!!ooooooo')