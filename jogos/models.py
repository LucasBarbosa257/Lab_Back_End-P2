from django.db import models

class Jogo(models.Model):
    STATUS_CHOICES = [
        ('anunciado', 'Anunciado'),
        ('pre_venda', 'Pré-Venda'), 
        ('lancado', 'Lançado'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=150)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='anunciado'
    )

    def __str__(self):
        return self.titulo