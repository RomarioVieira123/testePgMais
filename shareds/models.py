from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=60, default='')
    name_pt = models.CharField(max_length=60, default='')
    sigla = models.CharField(max_length=4, default='', blank=True)
    bacen = models.CharField(max_length=10, default='', blank=True)


class Stat(models.Model):
    name = models.CharField(max_length=75, default='')
    uf = models.CharField(max_length=2, default='')
    ibge = models.CharField(max_length=7, default='', blank=True)
    ddd = models.CharField(max_length=50, default='', blank=True)


class City(models.Model):
    name = models.CharField(max_length=120, default='')
    uf = models.CharField(max_length=2, default='')
    ibge = models.CharField(max_length=7, default='', blank=True)














