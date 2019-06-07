from django.db import models

class Core(models.Model):
    image = models.ImageField(upload_to='images/')
    fatia = models.IntegerField()
    tela = models.IntegerField()
