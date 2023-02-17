from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse 

from .forms import CopMembershipForm, RegistrationForm
from .models import CopMembership

# Create your views here.

def index(request):
    return render(request, 'copSite/index.html')

def user_dashboard(request):
    if not request.user.is_authenticated: #If the user has no account or if the user have not yet register.
        return redirect('copSite:login')
    else:
        cop_memb = CopMembership.objects.all()
        context = {'cop_memb': cop_memb}
        return render(request, 'copSite/user_dashboard.html', context)
    

def login_view(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not username or not password:
                messages.warning(request, 'Both username and password are required')
                return redirect('copSite:login')
            
            user_obj = User.objects.filter(username=username).first()
            if user_obj is None:
                messages.warning(request, 'User not found!')
                return redirect('copSite:login')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('copSite:user_dashboard'))
            else:
                if user != password:
                    messages.warning(request, 'Incorrect password!')
                    return redirect('copSite:login')
                
    except Exception as e:
        print(e)
    return render(request, 'copSite/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You've just logout of your account.")
    return render(request, 'copSite/login.html')

def signup_form(request):
    try:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('copSite:login')
        else:
            form = RegistrationForm()
            context = {"form": form}        
    except Exception as e:
        print(e)
    return render(request, 'copSite/signup.html', context)

def cop_membership_form(request):
    if request.method == 'POST':
        form = CopMembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('copSite:user_dashboard')
        else:
            
            return render(request, 'copSite/membership_form.html', {'form': form})
    else:
        form = CopMembershipForm()
        context = {"form": form}
        return render(request, 'copSite/membership_form.html', context)

