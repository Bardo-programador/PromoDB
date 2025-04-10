from django.db import models

# Create your models here.
class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    link = models.URLField()
    loja = models.CharField(max_length=100)