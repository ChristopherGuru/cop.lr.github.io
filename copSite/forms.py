from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CopMembership

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CopMembershipForm(ModelForm):
    class Meta:
        model = CopMembership
        # Email, Middle name will be optional.
        fields = [
            'suffix', 'f_name', 'm_name', 'l_name', 'birth_date', 'city_of_birth',
            'district_of_birth', 'county_of_orgin', 'nationality', 'current_address', 'phone_num', 'email',
            'occupation'
            ]
        
