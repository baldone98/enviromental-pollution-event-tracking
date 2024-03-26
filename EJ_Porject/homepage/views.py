from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

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

