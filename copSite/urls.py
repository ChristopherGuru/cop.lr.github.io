from django.urls import path 
from . import views 

app_name = "copSite"

urlpatterns = [
    path('', views.index, name='index'), # This is the general home page for the entired web application.

    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    path('register', views.signup_form, name='register'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'), # This is the route for a authenticated user.

    path('member_form', views.cop_membership_form, name='membership_form'), # This is route discribe the form that will be render to the user
    
]