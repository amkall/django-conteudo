from django.db import models

# Create your models here.

class Item(models.Model):
    nome = models.CharField(max_length = 255)
    preco = models.IntegerField()
    descricao = models.CharField(max_length = 512)
    url_img = models.CharField(max_length = 255) 

    def __str__(self):
        return self.nome