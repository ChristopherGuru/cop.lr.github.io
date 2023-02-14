from django.urls import path 
from . import views 

app_name = "copSite"

urlpatterns = [
    path('home', views.index, name='index'),
]