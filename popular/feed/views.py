# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from.utils import fetch_popular_from_dribble
from .models import Entrada

def home(request):
    dados = fetch_popular_from_dribble()
    contexto = {'shots': dados.get('shots', None)}
    return render(request, 'home.html', contexto)

def shot(request, shot_id):
    shot = get_object_or_404(Entrada, dribble_id=shot_id)
    return render(request, 'shot.html', shot.to_dict())