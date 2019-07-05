from __future__ import print_function
import sys
from django.shortcuts import render, get_object_or_404
from .models import EstruturaSite, Cidade, VideoCidade, VideoNarrativa, TipoVideo, TipoNarrativa, Bloco
import urllib
import requests


YOUTUBE_API_KEY ='AIzaSyC1L4Bn6qrFV-87tuhUFs-eVYBGMu1QhXQ'

def home(request):
    return render (request, 'core/home.html')

def narrativas(request, cidade_id ):

    cidades = Cidade.objects
    cidade = get_object_or_404(Cidade, pk=cidade_id)
    estruturaSite = EstruturaSite.objects
    estruturaSite = estruturaSite.filter(BlocoSite='Narrativas').first()
    videoNarrativa = VideoNarrativa.objects.all()

    ListaVideosNarrativas = []

    for v in videoNarrativa:
       videoN = video()
       parsed_url = urllib.parse.urlparse(v.VideoUrl)
       videoN.id = urllib.parse.parse_qs(parsed_url.query).get('v')
       videoN.TipoNarrativa = v.Modelo
       response = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={ videoN.id[0] }&key={ YOUTUBE_API_KEY }')
       json = response.json()

       videoN.thumb =  json['items'][0]['snippet']['thumbnails']['default']['url']
       print(videoN.thumb )
       ListaVideosNarrativas.append(videoN)

    return render (request, 'core/narrativas.html', {'Cidades': cidades, 'CidadePagina':cidade,
                    'BlocosSite':Bloco, 'EstruturaSite': estruturaSite, 'VideoNarrativaThumbs': ListaVideosNarrativas })



def estruturaSite(request, estruturaSiteNome):
    #cidade = get_object_or_404(Cidade, pk=estruturaSite_id)
    #return render (request, 'core/espacos_contem.html')
#    blocosSite = Bloco.objects
    cidades = Cidade.objects
    estruturaSite = EstruturaSite.objects
    estruturaSite = estruturaSite.filter(BlocoSite= estruturaSiteNome).first()
    ##estruturaSite = estruturaSite.filter()[:1].get()

    return render (request, 'core/estrutura.html', {'Cidades': cidades, 'EstruturaSite': estruturaSite,'BlocosSite':Bloco  })


def contato(request):
    return render (request, 'core/contato.html')

def apresenta(request):
    return render (request, 'core/apresenta.html')

def equipe(request):
    return render (request, 'core/equipe.html')


class video:
    thumb =[]
