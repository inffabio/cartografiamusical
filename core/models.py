from django.db import models



class Cidade(models.Model):
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return format(self.descricao)

class TipoMusica(models.Model):
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return format(self.descricao)


class Local(models.Model):
    descricao = models.CharField(max_length=500)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    Latitude = models.CharField(max_length=500)
    Longitude = models.CharField(max_length=500)
    def __str__(self):
        return format(self.descricao)


class Imagem(models.Model):

    imagem = models.ImageField(upload_to='images/')
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    TipoMusica = models.ForeignKey(TipoMusica, on_delete=models.CASCADE)



class Video(models.Model):

    url = models.CharField(max_length=500)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    TipoMusica = models.ForeignKey(TipoMusica, on_delete=models.CASCADE)
    def __str__(self):
        return format(self.url)
