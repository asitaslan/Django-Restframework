from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Makale(models. Model):
    baslik = models.CharField(max_length=150)
    yazar = models.CharField(max_length=150)
    aciklama = models.CharField(max_length=200)
    metin = models.TextField()
    sehir = models.CharField(max_length=75)
    yayinlanma_tarihi = models.DateField()
    aktif = models.BooleanField(default=True)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.baslik