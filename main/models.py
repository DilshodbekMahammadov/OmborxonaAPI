from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator

class Bolim(models.Model):
    nom = models.CharField(max_length=250)

    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=250)
    brend = models.CharField(max_length=250, blank=True, null=True)
    narx1 = models.FloatField(validators=[MinValueValidator(0.0)])
    narx2 = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
    miqdor = models.FloatField(validators=[MinValueValidator(0.0)])
    olchov = models.CharField(max_length=10, blank=True, null=True)
    oxirgi_sana = models.DateTimeField(blank=True, null=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Mijoz(models.Model):
    ism = models.CharField(max_length=250)
    dokon = models.CharField(max_length=250)
    tel = models.CharField(max_length=15)
    manzil = models.TextField(blank=True, null=True)
    qarz = models.FloatField(validators=[MinValueValidator(0.0)], null=True, blank=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.ism

class Sotuv(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.FloatField(validators=[MinValueValidator(0.0)])
    sana = models.DateTimeField(auto_now_add=True)
    jami_summa = models.FloatField(validators=[MinValueValidator(0.0)])
    tolandi = models.FloatField(validators=[MinValueValidator(0.0)])
    qarz = models.FloatField(validators=[MinValueValidator(0.0)])
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mahsulot} {self.miqdor}"

class Sotuvchi(models.Model):
    rasm = models.ImageField(upload_to='sotuvchilar/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username