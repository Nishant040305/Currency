from django.db import models

# Create your models here.
class favPain(models.Model):
    serialNumber = models.AutoField
    fromCode = models.CharField(max_length=(5))
    toCode = models.CharField(max_length=(5))
class History(models.Model):
    serialNumber = models.AutoField
    fcurrencyCode=models.CharField(max_length=(5))
    fAmount = models.CharField(max_length=(50))
    tcurrencyCode = models.CharField(max_length=(5))
    tAmount = models.CharField(max_length=(50))
