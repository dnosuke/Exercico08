from django.db import models


class Despesa(models.Model):

    cliente = models.CharField('cliente', max_length=200,)
    produto = models.CharField('produto', max_length=200,)
    fornecedor = models.CharField('fornecedor', max_length=200,)
    descricao = models.CharField('descrição', max_length=200,)

    class Meta:
        verbose_name_plural= ''
        verbose_name= ''

    def __str__(self):
        return self.cliente



