from django.db import models

class CropSuggestion(models.Model):
    N=models.IntegerField()
    P=models.IntegerField()
    K=models.IntegerField()
    Temprture=models.DecimalField(max_digits=5, decimal_places=2)
    Humidity=models.DecimalField(max_digits=5, decimal_places=2)
    ph=models.DecimalField(max_digits=5, decimal_places=2)
    rainfall=models.DecimalField(max_digits=5, decimal_places=2)
    