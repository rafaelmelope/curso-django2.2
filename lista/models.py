from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

"""
Post
--------
author
title
text
created_date
published_date
publish()
"""

ESTADOS = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
)


class Lista(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.expire_date = timezone.now()
        self.save()

    def __str__(self):
        # return "Titulo: {} e Subtitulo {}".format(self.title, self.subtitle)
        return self.title

    class Meta:
        ordering = ['created_date']
        # ordering = ['-created_date']
        verbose_name = 'Lista de Compra'
        verbose_name_plural = 'Lista de Compras'
