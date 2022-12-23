from django.forms import ModelForm
from .models import CropSuggestion
class Suggestionsfrom(ModelForm):
    class Meta:
        model=CropSuggestion
        fields=['N','P','K','Temprture','Humidity','ph','rainfall']
        
