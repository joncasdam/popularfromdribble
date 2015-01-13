# -*- encoding: utf-8 -*-
import os
from urlparse import urlparse
import urllib2

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


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