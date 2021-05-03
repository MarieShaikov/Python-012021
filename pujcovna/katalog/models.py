from django.db import models

# Create your models here.


class Auto(models.Model):
  number_plate = models.CharField(max_length=100)
  car_typ = models.CharField(max_length=100)
  km_total = models.IntegerField()
  last_control = models.DateField()


class Zakaznik(models.Model):
  name = models.CharField(max_length=100)
  surname = models.CharField(max_length=100)
  driving_license = models.CharField(max_length=100)
  birthdate = models.DateField()


class Vypujcka(models.Model):
  rent_start = models.DateTimeField()
  rent_end = models.DateTimeField()
  price = models.IntegerField()
