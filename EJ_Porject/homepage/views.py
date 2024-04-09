from django.shortcuts import render, redirect 
from django.template import loader
from django.http import HttpResponse

#Imported for use with login
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages

###JKK
import csv
import os
#JKK###

def index(request): 
    return render(request, "homepage/index.html")

def search_view(request):
    return render(request, "search/search.html")

def report_view(request):
    return render(request, "report/report.html")

def wordcloud_view(request):
    return render(request, "wordcloud/wordcloud.html")

def maptracking_view(request):
    return render(request, "maptracking/maptracking.html")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered! Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return redirect('report')  # Change 'home' to your desired homepage
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'login/login.html', {'form': form})