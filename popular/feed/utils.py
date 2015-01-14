# -*- encoding: utf-8 -*-
import os
from urlparse import urlparse
import urllib2
import simplejson as json

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.conf import settings


def download_image(url):
    nome = urlparse(url).path.split('/')[-1]
    img_temp = NamedTemporaryFile(delete=True)
    try:
        img_temp.write(urllib2.urlopen(url).read())
        img_temp.flush()
        file_stats = os.stat(img_temp.name)
        if file_stats.st_size:
            return nome, File(img_temp)
    except:
        pass

    return None, None

def fetch_popular_from_dribble():
    try:
        req = urllib2.Request(settings.DRIBBLE_POPULAR_URL)
        resposta = urllib2.urlopen(req).read()
        dados = json.loads(resposta)
        return dados
    except:
        pass
    return None