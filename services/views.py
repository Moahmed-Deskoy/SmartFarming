from audioop import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from .form import Suggestionsfrom   
def crop_Suggestions(request):
    if request.method=='POST':
      suggest_form=Suggestionsfrom(request.POST)
    else:
        suggest_form=Suggestionsfrom() 
    context={'suggest_form':suggest_form}  
    return (render(request,'suggest/suggest.html'))
def crop_predictions(request):
    return (render(request,'predict/predict.html'))
