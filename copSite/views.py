from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse 

from .forms import RegistrationForm
# Create your views here.

def index(request):
    return render(request, 'copSite/index.html')

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
            if user_obj and not password:
                messages.warning(request, 'Incorrect password!')
                return redirect('copSite:login')
            user = authenticate(request, username=username, password=password)
            if user is None:
                login(request, user)
                return HttpResponseRedirect(reverse(''))
    except Exception as e:
        print(e)
    return render(request, 'copSite/login.html')

def signup_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = RegistrationForm()
        context = {"form": form}
        return render(request, 'copSite/signup.html', context)