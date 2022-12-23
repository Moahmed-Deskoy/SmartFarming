app_name='services'
from django.urls import path,include
from . import views

urlpatterns = [
    path('crop_Suggestions', views.crop_Suggestions,name='crop_Suggestions'),
    path('crop_predictions', views.crop_predictions,name='crop_predictions'),
]

