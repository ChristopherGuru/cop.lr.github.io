from django.urls import path 
from . import views 

app_name = "copSite"

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('register', views.signup_form, name='register'),
]