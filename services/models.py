from django.db import models

class CropSuggestion(models.Model):
    N=models.IntegerField()
    P=models.IntegerField()
    K=models.IntegerField()
    Temperature=models.DecimalField(max_digits=5, decimal_places=5)
    Humidity=models.DecimalField(max_digits=5, decimal_places=5)
    ph=models.DecimalField(max_digits=5, decimal_places=5)
    rainfall=models.DecimalField(max_digits=5, decimal_places=5)
    