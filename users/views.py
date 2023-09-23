from django.shortcuts import render
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

# Home

def home_view(request):
    return render(request, 'home.html')

# Dashboard

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})

# Register

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout
 
def logout_view(request):
    logout(request)
    return redirect('home')