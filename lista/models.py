from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

class Lista(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField()
    # expire_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.expire_date = timezone.now()
        self.save()

    def __str__(self):
        # return "Titulo: {} e Subtitulo {}".format(self.title, self.subtitle)
        return self.title

    class Meta:
        # ordering = ['created_date']
        ordering = ['-created_date']
        verbose_name = 'Lista de Compra'
        verbose_name_plural = 'Lista de Compras'
