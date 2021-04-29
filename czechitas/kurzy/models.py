from django.db import models

# Create your models here.

from django.db import models


class Kurz(models.Model):
  nazev = models.CharField(max_length=100)
  zacatek = models.DateTimeField()
  konec = models.DateTimeField()
  popis = models.CharField(max_length=1000)
  cena = models.IntegerField()

class Detail_organizace (DetailView):
  model=models.Organizace
  template_name = "organizace_detail.html"

class Prihlaska(models.Model):
  email = models.CharField(max_length=100)
  jmeno = models.CharField(max_length=100)
  prijmeni = models.CharField(max_length=100)
  motivace = models.TextField()
  kurz = models.ForeignKey(Kurz, on_delete=models.SET_NULL, null=True)