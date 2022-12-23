from django import forms
from .models import CropSuggestion
class cropSuggestionForm(forms.ModelForm):
    class Meta:    
        model=CropSuggestion
        fields='__all__'