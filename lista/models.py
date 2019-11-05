from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

class Lista(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.localdate)
    # created_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField()
    # expire_date = models.DateTimeField(blank=True, null=
    valid = models.BooleanField(default=False)
    dias = models.CharField(max_length=4)
    atencao = models.BooleanField(default=False)

    def publish(self):
        self.expire_date = timezone.localdate()
        self.save()

    def expire(self):
        self.valid = self.expire_date.date() < timezone.localdate()
        self.save()

    def __str__(self):
        # return "Titulo: {} e Subtitulo {}".format(self.title, self.subtitle)
        return self.title

    class Meta:
        # ordering = ['-created_date']
        ordering = ['expire_date']
        verbose_name = 'Lista de Compra'
        verbose_name_plural = 'Lista de Compras'
