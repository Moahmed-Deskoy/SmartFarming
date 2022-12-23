from audioop import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from .form import cropSuggestionForm   
def crop_Suggestions(request):
    if request.method=='POST':
        form=cropSuggestionForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.save()           
    else:
        form=cropSuggestionForm()    
    context={'form':form}
    return render(request,'suggest/suggest.html',context)

def crop_predictions(request):
    return (render(request,'predict/predict.html'))
