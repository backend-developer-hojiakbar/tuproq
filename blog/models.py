from datetime import timezone

from django.db import models
from django.utils import timezone
# Create your models here.

class Royxat(models.Model):
    ism = models.CharField(max_length=500)
    tel_raqam = models.IntegerField()

    def __str__(self):
        return self.ism
class Yangiliklar(models.Model):
    rasm = models.ImageField(upload_to='rasmlar/images')
    text = models.TextField()
    nom = models.CharField(max_length=1000)
    chopetilishVaqti = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-chopetilishVaqti']
    objects = models.Manager()

    def __str__(self):
        return self.nom
class Bizhaqimizda_rasm(models.Model):
    rasm = models.ImageField(upload_to='rasmlar/images')
    nom = models.CharField(max_length=200)
class SONGI_YILLARDA_BAJARILGAN_ISHLAR_XAJMI(models.Model):
    rasm = models.ImageField(upload_to='rasmlar/images')
    text = models.TextField()
    text1 = models.TextField()
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom
class FuterManzil(models.Model):
    email = models.CharField(max_length=200)
    manzil = models.TextField()
    tel_raqam1 = models.IntegerField()
    tel_raqam2 = models.IntegerField()

    def __str__(self):
        return self.email