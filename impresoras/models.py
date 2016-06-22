from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
        #centro = models.ForeignKey('auth.User')
        centro = models.CharField(max_length=200)
        cid = models.CharField(max_length=20)
        modelo = models.CharField(max_length=200)
        descripcion = models.TextField()
        numero_copias = models.IntegerField()
        numero_hojas = models.IntegerField()
        fecha = models.DateTimeField(
                default=timezone.now)
        fecha_publicacion = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.fecha_publicacion = timezone.now()
            self.save()

        def __str__(self):
            return self.modelo
