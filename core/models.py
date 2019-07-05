from django.db import models
from django.contrib.auth.models import User
from enum import Enum


def forDjango(cls):
    cls.do_not_call_in_templates = True
    return cls

@forDjango
class TipoVideo(Enum):
    MUGR = "Músicas/Grupos"
    NARR = "Narrativas"
    CORP = "Corpos"

@forDjango
class TipoNarrativa(Enum):
    MUSI = "Músicos"
    FREQ = "Frequentadores - Fãs - Consumidores"
    OUTR = "Outras Vozes"



@forDjango
class Bloco(Enum):
    Espacos = "Espaços"
    Musicas = "Músicas"
    Grupos = "Grupos"
    Corpos = "Corpos"
    Narrativas = "Narrativas"




class Cidade(models.Model):
    Nome = models.CharField(max_length=100)
    Imagem = models.ImageField(upload_to='images/')
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return format(self.Nome)

class VideoCidade(models.Model):
    Nome = models.CharField(max_length=100)
    VideoUrl = models.CharField(max_length=500)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    Modelo = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in TipoVideo])
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return format(self.Nome)

class EstruturaSite(models.Model):
    Nome = models.CharField(max_length=100)
    Descricao = models.TextField()
    Imagem = models.ImageField(upload_to='images/')
    BlocoSite = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Bloco])
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return format(self.Nome)


class VideoNarrativa(models.Model):
    Nome = models.CharField(max_length=100)
    VideoUrl = models.CharField(max_length=500)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    Modelo = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in TipoNarrativa])
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return format(self.Nome)


"""
class TipoMusica(models.Model):
    descricao = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return format(self.descricao)
"""

"""
class Local(models.Model):
    descricao = models.CharField(max_length=500)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    Latitude = models.CharField(max_length=500)
    Longitude = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return format(self.descricao)
"""

"""
class Imagem(models.Model):

    Nome = models.CharField(max_length=100)
    Imagem = models.ImageField(upload_to='images/')
    Local = models.ForeignKey(Local, on_delete=models.CASCADE)
    TipoMusica = models.ForeignKey(TipoMusica, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
"""
